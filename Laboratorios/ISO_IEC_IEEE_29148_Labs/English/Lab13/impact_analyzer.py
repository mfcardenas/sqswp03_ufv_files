#!/usr/bin/env python3
"""
Requirements Impact Analyzer Module
ISO/IEC/IEEE 29148:2011 Impact Analysis Implementation
"""

import json
import os
import sys
import logging
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict, Any, Optional, Union, Tuple, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("impact_analysis.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ImpactAnalyzer:
    """Main class for impact analysis"""
    
    def __init__(self, config_file: str):
        """
        Initialize impact analyzer
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = {}
        self.requirements = {}
        self.dependency_graph = nx.DiGraph()
        self.storage_file = "impact_analysis.json"
        self.is_initialized = False
        self.initialize()
    
    def initialize(self) -> None:
        """Initialize the impact analyzer"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            # Load requirement data if available
            self._load_requirements()
            
            # Build dependency graph
            self._build_dependency_graph()
            
            self.is_initialized = True
            logger.info("Impact analyzer initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize impact analyzer: {str(e)}")
            self.is_initialized = False
    
    def _load_requirements(self) -> None:
        """Load requirements data"""
        try:
            # Try to load from requirements file
            requirements_file = self.config.get("requirementsFile", "requirements.json")
            
            if os.path.exists(requirements_file):
                with open(requirements_file, 'r') as f:
                    self.requirements = json.load(f)
                logger.info(f"Loaded {len(self.requirements)} requirements from {requirements_file}")
            else:
                # Use requirements from config if available
                self.requirements = self.config.get("requirements", {})
                logger.info(f"Loaded {len(self.requirements)} requirements from config")
        except Exception as e:
            logger.error(f"Failed to load requirements: {str(e)}")
            self.requirements = {}
    
    def _build_dependency_graph(self) -> None:
        """Build dependency graph from requirements"""
        try:
            # Create a new directed graph
            self.dependency_graph = nx.DiGraph()
            
            # Add nodes for each requirement
            for req_id, requirement in self.requirements.items():
                self.dependency_graph.add_node(req_id, **requirement)
            
            # Add edges for dependencies
            for req_id, requirement in self.requirements.items():
                dependencies = requirement.get("dependencies", [])
                for dep in dependencies:
                    if dep in self.requirements:
                        self.dependency_graph.add_edge(req_id, dep)
            
            logger.info(f"Built dependency graph with {self.dependency_graph.number_of_nodes()} nodes and {self.dependency_graph.number_of_edges()} edges")
        except Exception as e:
            logger.error(f"Failed to build dependency graph: {str(e)}")
            self.dependency_graph = nx.DiGraph()
    
    def analyze_impact(self, requirement_ids: List[str]) -> Dict[str, Any]:
        """
        Analyze the impact of changing requirements
        
        Args:
            requirement_ids: List of requirement IDs to analyze
            
        Returns:
            Dict[str, Any]: Impact analysis results
        """
        if not self.is_initialized:
            logger.error("Impact analyzer not initialized")
            return {"error": "Impact analyzer not initialized"}
        
        # Validate requirement IDs
        invalid_ids = [req_id for req_id in requirement_ids if req_id not in self.requirements]
        if invalid_ids:
            logger.warning(f"Invalid requirement IDs: {invalid_ids}")
            return {"error": f"Invalid requirement IDs: {invalid_ids}"}
        
        # Perform impact analysis
        try:
            # Get directly affected requirements (outgoing edges)
            directly_affected = set()
            for req_id in requirement_ids:
                directly_affected.update(list(self.dependency_graph.successors(req_id)))
            
            # Get indirectly affected requirements (downstream dependencies)
            indirectly_affected = set()
            for req_id in requirement_ids:
                descendants = nx.descendants(self.dependency_graph, req_id)
                indirectly_affected.update(descendants - directly_affected - set(requirement_ids))
            
            # Get upstream dependencies (requirements that depend on the changed ones)
            upstream_dependencies = set()
            for req_id in requirement_ids:
                ancestors = nx.ancestors(self.dependency_graph, req_id)
                upstream_dependencies.update(ancestors)
            
            # Calculate risk scores
            risk_scores = self._calculate_risk_scores(requirement_ids, directly_affected, indirectly_affected)
            
            # Prepare result
            result = {
                "analyzed_requirements": requirement_ids,
                "directly_affected": list(directly_affected),
                "indirectly_affected": list(indirectly_affected),
                "upstream_dependencies": list(upstream_dependencies),
                "total_impact_count": len(directly_affected) + len(indirectly_affected),
                "risk_assessment": {
                    "overall_risk_level": self._get_overall_risk_level(risk_scores),
                    "risk_scores": risk_scores
                },
                "affected_categories": self._get_affected_categories(directly_affected, indirectly_affected),
                "timestamp": self.get_timestamp()
            }
            
            logger.info(f"Completed impact analysis for {len(requirement_ids)} requirements")
            return result
        except Exception as e:
            logger.error(f"Failed to analyze impact: {str(e)}")
            return {"error": f"Failed to analyze impact: {str(e)}"}
    
    def _calculate_risk_scores(self, changed_reqs: List[str], direct_impact: Set[str], indirect_impact: Set[str]) -> Dict[str, Any]:
        """
        Calculate risk scores for impact analysis
        
        Args:
            changed_reqs: Requirements being changed
            direct_impact: Directly affected requirements
            indirect_impact: Indirectly affected requirements
            
        Returns:
            Dict[str, Any]: Risk score data
        """
        # Initialize risk score categories
        risk_scores = {
            "scope_risk": 0,
            "complexity_risk": 0,
            "schedule_risk": 0,
            "quality_risk": 0,
            "technical_risk": 0
        }
        
        # Count impact by priority
        priority_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        
        # Calculate scope risk based on number of affected requirements
        total_affected = len(direct_impact) + len(indirect_impact)
        total_reqs = len(self.requirements)
        
        # Scope risk (0-100)
        scope_percentage = (total_affected / total_reqs) * 100 if total_reqs > 0 else 0
        risk_scores["scope_risk"] = min(100, scope_percentage)
        
        # Analyze affected requirements by priority
        for req_id in direct_impact.union(indirect_impact):
            req = self.requirements.get(req_id, {})
            priority = req.get("priority", "medium").lower()
            if priority in priority_counts:
                priority_counts[priority] += 1
        
        # Complexity risk based on dependencies and affected priorities
        complexity_score = 0
        complexity_score += priority_counts["critical"] * 10
        complexity_score += priority_counts["high"] * 5
        complexity_score += priority_counts["medium"] * 2
        complexity_score += priority_counts["low"] * 1
        
        # Normalize complexity score (0-100)
        risk_scores["complexity_risk"] = min(100, complexity_score)
        
        # Schedule risk based on complexity and scope
        risk_scores["schedule_risk"] = min(100, (risk_scores["scope_risk"] + risk_scores["complexity_risk"]) / 2)
        
        # Quality risk based on criticality of affected requirements
        quality_score = 0
        quality_score += priority_counts["critical"] * 15
        quality_score += priority_counts["high"] * 8
        quality_score += priority_counts["medium"] * 3
        
        # Normalize quality score (0-100)
        risk_scores["quality_risk"] = min(100, quality_score)
        
        # Technical risk based on dependency depth
        max_depth = 0
        for req_id in changed_reqs:
            # Find the maximum path length from this requirement
            for affected in indirect_impact:
                try:
                    path_length = len(nx.shortest_path(self.dependency_graph, req_id, affected)) - 1
                    max_depth = max(max_depth, path_length)
                except nx.NetworkXNoPath:
                    continue
        
        # Normalize technical risk (0-100)
        risk_scores["technical_risk"] = min(100, max_depth * 20)  # 20 points per depth level
        
        return risk_scores
    
    def _get_overall_risk_level(self, risk_scores: Dict[str, float]) -> str:
        """
        Determine overall risk level from risk scores
        
        Args:
            risk_scores: Risk scores by category
            
        Returns:
            str: Overall risk level (low, medium, high, critical)
        """
        # Calculate average risk score
        avg_score = sum(risk_scores.values()) / len(risk_scores)
        
        # Determine risk level
        if avg_score >= 75:
            return "critical"
        elif avg_score >= 50:
            return "high"
        elif avg_score >= 25:
            return "medium"
        else:
            return "low"
    
    def _get_affected_categories(self, direct_impact: Set[str], indirect_impact: Set[str]) -> Dict[str, int]:
        """
        Get counts of affected requirements by category
        
        Args:
            direct_impact: Directly affected requirements
            indirect_impact: Indirectly affected requirements
            
        Returns:
            Dict[str, int]: Counts by category
        """
        categories = {}
        
        # Count affected requirements by category
        for req_id in direct_impact.union(indirect_impact):
            req = self.requirements.get(req_id, {})
            category = req.get("category", "uncategorized")
            
            if category not in categories:
                categories[category] = 0
            
            categories[category] += 1
        
        return categories
    
    def visualize_impact(self, requirement_ids: List[str], output_file: str = "impact_analysis.png") -> bool:
        """
        Visualize impact analysis as a network graph
        
        Args:
            requirement_ids: List of requirement IDs to analyze
            output_file: Path to output image file
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.is_initialized:
            logger.error("Impact analyzer not initialized")
            return False
        
        try:
            # Create a subgraph for visualization
            affected_nodes = set(requirement_ids)
            
            # Add directly affected nodes
            for req_id in requirement_ids:
                affected_nodes.update(list(self.dependency_graph.successors(req_id)))
            
            # Add indirectly affected nodes (up to 2 levels)
            for req_id in list(affected_nodes):
                if req_id in self.dependency_graph:
                    successors = list(self.dependency_graph.successors(req_id))
                    affected_nodes.update(successors)
                    
                    # Add one more level
                    for succ in successors:
                        if succ in self.dependency_graph:
                            affected_nodes.update(list(self.dependency_graph.successors(succ)))
            
            # Create subgraph
            impact_graph = self.dependency_graph.subgraph(affected_nodes)
            
            # Set up colors and styles
            node_colors = []
            node_sizes = []
            
            for node in impact_graph.nodes():
                if node in requirement_ids:
                    node_colors.append('red')  # Changed requirements
                    node_sizes.append(800)
                elif node in [n for r in requirement_ids for n in self.dependency_graph.successors(r)]:
                    node_colors.append('orange')  # Directly affected
                    node_sizes.append(600)
                else:
                    node_colors.append('blue')  # Indirectly affected
                    node_sizes.append(400)
            
            # Create figure
            plt.figure(figsize=(12, 8))
            
            # Set layout
            pos = nx.spring_layout(impact_graph, seed=42)
            
            # Draw nodes
            nx.draw_networkx_nodes(impact_graph, pos, node_color=node_colors, 
                                  node_size=node_sizes, alpha=0.8)
            
            # Draw edges
            nx.draw_networkx_edges(impact_graph, pos, width=1.0, alpha=0.5, 
                                  edge_color='gray', arrows=True)
            
            # Draw labels
            nx.draw_networkx_labels(impact_graph, pos, font_size=8, font_family='sans-serif')
            
            # Add title and legend
            plt.title(f"Impact Analysis for {', '.join(requirement_ids)}")
            
            # Add legend
            legend_elements = [
                plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Changed'),
                plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='Directly Affected'),
                plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Indirectly Affected')
            ]
            plt.legend(handles=legend_elements, loc='upper right')
            
            # Remove axis
            plt.axis('off')
            
            # Save figure
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            plt.close()
            
            logger.info(f"Generated impact visualization: {output_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to visualize impact: {str(e)}")
            return False
    
    def get_impact_metrics(self, requirement_ids: List[str]) -> Dict[str, Any]:
        """
        Get metrics for impact analysis
        
        Args:
            requirement_ids: List of requirement IDs to analyze
            
        Returns:
            Dict[str, Any]: Impact metrics
        """
        # Perform impact analysis
        impact_results = self.analyze_impact(requirement_ids)
        
        if "error" in impact_results:
            return impact_results
        
        # Calculate additional metrics
        try:
            # Get counts
            directly_affected = impact_results["directly_affected"]
            indirectly_affected = impact_results["indirectly_affected"]
            upstream_dependencies = impact_results["upstream_dependencies"]
            
            # Calculate complexity metrics
            avg_outdegree = 0
            max_outdegree = 0
            
            for req_id in requirement_ids:
                if req_id in self.dependency_graph:
                    outdegree = self.dependency_graph.out_degree(req_id)
                    avg_outdegree += outdegree
                    max_outdegree = max(max_outdegree, outdegree)
            
            if requirement_ids:
                avg_outdegree /= len(requirement_ids)
            
            # Calculate ripple effect ratio
            total_reqs = len(self.requirements)
            ripple_effect = (len(directly_affected) + len(indirectly_affected)) / total_reqs if total_reqs > 0 else 0
            
            # Prepare metrics
            metrics = {
                "impact_count": {
                    "directly_affected": len(directly_affected),
                    "indirectly_affected": len(indirectly_affected),
                    "upstream_dependencies": len(upstream_dependencies),
                    "total_impact": len(directly_affected) + len(indirectly_affected)
                },
                "complexity_metrics": {
                    "avg_dependencies_per_requirement": avg_outdegree,
                    "max_dependencies": max_outdegree,
                    "ripple_effect_ratio": ripple_effect,
                    "impact_percentage": ripple_effect * 100
                },
                "risk_assessment": impact_results["risk_assessment"],
                "timestamp": self.get_timestamp()
            }
            
            logger.info(f"Generated impact metrics for {len(requirement_ids)} requirements")
            return metrics
        except Exception as e:
            logger.error(f"Failed to generate impact metrics: {str(e)}")
            return {"error": f"Failed to generate impact metrics: {str(e)}"}
    
    def get_critical_requirements(self) -> List[Dict[str, Any]]:
        """
        Identify critical requirements based on dependency analysis
        
        Returns:
            List[Dict[str, Any]]: List of critical requirements with metrics
        """
        if not self.is_initialized:
            logger.error("Impact analyzer not initialized")
            return []
        
        try:
            critical_reqs = []
            
            # Calculate centrality measures
            out_degree = dict(self.dependency_graph.out_degree())
            in_degree = dict(self.dependency_graph.in_degree())
            
            # Calculate betweenness centrality (may be slow for large graphs)
            betweenness = nx.betweenness_centrality(self.dependency_graph)
            
            # Identify critical requirements
            for req_id, requirement in self.requirements.items():
                # Skip requirements that are not in the graph
                if req_id not in self.dependency_graph:
                    continue
                
                # Calculate metrics
                impact_count = out_degree.get(req_id, 0)
                dependent_count = in_degree.get(req_id, 0)
                centrality = betweenness.get(req_id, 0)
                
                # Calculate criticality score
                criticality = (impact_count * 0.4) + (dependent_count * 0.4) + (centrality * 100 * 0.2)
                
                # Add to list if metrics are significant
                if impact_count > 0 or dependent_count > 0 or centrality > 0:
                    critical_reqs.append({
                        "id": req_id,
                        "title": requirement.get("title", "Untitled"),
                        "impact_count": impact_count,
                        "dependent_count": dependent_count,
                        "centrality": centrality,
                        "criticality_score": criticality,
                        "priority": requirement.get("priority", "medium"),
                        "category": requirement.get("category", "uncategorized")
                    })
            
            # Sort by criticality score
            critical_reqs.sort(key=lambda x: x["criticality_score"], reverse=True)
            
            logger.info(f"Identified {len(critical_reqs)} critical requirements")
            return critical_reqs
        except Exception as e:
            logger.error(f"Failed to identify critical requirements: {str(e)}")
            return []
    
    def get_dependency_paths(self, source_id: str, target_id: str) -> List[List[str]]:
        """
        Get all dependency paths between two requirements
        
        Args:
            source_id: Source requirement ID
            target_id: Target requirement ID
            
        Returns:
            List[List[str]]: List of paths (each path is a list of requirement IDs)
        """
        if not self.is_initialized:
            logger.error("Impact analyzer not initialized")
            return []
        
        try:
            # Check if requirements exist
            if source_id not in self.requirements or target_id not in self.requirements:
                logger.warning(f"Invalid requirement IDs: {source_id} or {target_id}")
                return []
            
            # Find all simple paths
            paths = list(nx.all_simple_paths(self.dependency_graph, source_id, target_id))
            
            logger.info(f"Found {len(paths)} dependency paths from {source_id} to {target_id}")
            return paths
        except Exception as e:
            logger.error(f"Failed to get dependency paths: {str(e)}")
            return []
    
    def export_impact_report(self, requirement_ids: List[str], output_file: str = "impact_report.json") -> bool:
        """
        Export impact analysis report to a file
        
        Args:
            requirement_ids: List of requirement IDs to analyze
            output_file: Path to output file
            
        Returns:
            bool: True if successful, False otherwise
        """
        # Perform impact analysis
        impact_results = self.analyze_impact(requirement_ids)
        
        if "error" in impact_results:
            return False
        
        try:
            # Add additional details to the report
            report = {
                "impact_analysis": impact_results,
                "metrics": self.get_impact_metrics(requirement_ids),
                "requirement_details": {
                    "changed_requirements": self._get_requirement_details(requirement_ids),
                    "directly_affected": self._get_requirement_details(impact_results["directly_affected"]),
                    "indirectly_affected": self._get_requirement_details(impact_results["indirectly_affected"])
                },
                "timestamp": self.get_timestamp(),
                "graph_statistics": {
                    "total_requirements": len(self.requirements),
                    "total_dependencies": self.dependency_graph.number_of_edges()
                }
            }
            
            # Write to file
            with open(output_file, 'w') as f:
                json.dump(report, f, indent=2)
            
            logger.info(f"Exported impact report to {output_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to export impact report: {str(e)}")
            return False
    
    def _get_requirement_details(self, requirement_ids: List[str]) -> Dict[str, Dict[str, Any]]:
        """
        Get details for a list of requirements
        
        Args:
            requirement_ids: List of requirement IDs
            
        Returns:
            Dict[str, Dict[str, Any]]: Requirement details
        """
        details = {}
        
        for req_id in requirement_ids:
            if req_id in self.requirements:
                details[req_id] = self.requirements[req_id]
        
        return details
    
    @staticmethod
    def get_timestamp() -> str:
        """
        Get current timestamp as ISO format
        
        Returns:
            str: ISO formatted timestamp
        """
        from datetime import datetime
        return datetime.now().isoformat()


if __name__ == '__main__':
    """Main entry point for standalone execution"""
    if len(sys.argv) < 2:
        print("Usage: python impact_analyzer.py <config_file> [requirement_ids...]")
        sys.exit(1)
    
    config_file = sys.argv[1]
    analyzer = ImpactAnalyzer(config_file)
    
    if not analyzer.is_initialized:
        print("Failed to initialize impact analyzer")
        sys.exit(1)
    
    print("Impact analyzer initialized successfully.")
    
    # Analyze impact if requirement IDs are provided
    if len(sys.argv) > 2:
        requirement_ids = sys.argv[2:]
        print(f"Analyzing impact for requirements: {', '.join(requirement_ids)}")
        
        impact_results = analyzer.analyze_impact(requirement_ids)
        
        if "error" in impact_results:
            print(f"Error: {impact_results['error']}")
            sys.exit(1)
        
        print("\nImpact Analysis Results:")
        print(f"Directly affected requirements: {len(impact_results['directly_affected'])}")
        print(f"Indirectly affected requirements: {len(impact_results['indirectly_affected'])}")
        print(f"Total impact count: {impact_results['total_impact_count']}")
        print(f"Overall risk level: {impact_results['risk_assessment']['overall_risk_level']}")
        
        # Visualize impact
        if analyzer.visualize_impact(requirement_ids):
            print(f"Impact visualization saved to impact_analysis.png")
        
        # Export report
        if analyzer.export_impact_report(requirement_ids):
            print(f"Impact report saved to impact_report.json")
    else:
        # Print critical requirements if no specific requirements are provided
        critical_reqs = analyzer.get_critical_requirements()
        
        print("\nTop 5 Critical Requirements:")
        for i, req in enumerate(critical_reqs[:5], 1):
            print(f"{i}. {req['id']} - {req['title']}")
            print(f"   Impact Count: {req['impact_count']}")
            print(f"   Dependent Count: {req['dependent_count']}")
            print(f"   Criticality Score: {req['criticality_score']:.2f}")
            print()
