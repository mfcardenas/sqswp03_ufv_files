# 📚 Project Documentation – ISO Educational Materials

## 🎯 Purpose

This is the **standalone navigable documentation** for the complete Educational Materials project for Software Engineering. It was created specifically for:

- **📡 Public server deployment:** Fully navigable website with zero external dependencies
- **🎮 Educational games bundle:** Every HTML/CSS/JS game integrated into the documentation hub
- **🌐 Unified navigation:** Cross-linking between sections for a seamless experience
- **📖 Professional presentation:** Ready to showcase to stakeholders and students

## 📂 Project Structure

```
Documentación/
├── index.html                    # Main landing (Spanish)
├── index_es.html                 # Main landing (Spanish)
├── index_en.html                 # Main landing (English)
├── README.md                     # This file
├── Laboratorios/
│   ├── ISO_9241_Labs/
│   │   ├── lab1_es.html          # Lab 1 - User Context Analysis (ES)
│   │   ├── lab1_en.html          # Lab 1 - User Context Analysis (EN)
│   │   ├── lab2_en.html          # Lab 2 - Dialogue Principles
│   │   ├── lab3_en.html          # Lab 3 - Heuristic Evaluation
│   │   ├── lab5_en.html          # Lab 5 - Usability Testing
│   │   ├── lab6_en.html          # Lab 6 - Human-Centered Design
│   │   ├── iso_9241_labs.html    # Lab index (Spanish)
│   │   └── iso_9241_labs_en.html # Lab index (English)
│   ├── ISO_IEC_IEEE_29148_Labs/
│   │   ├── iso_29148_labs.html    # ISO 29148 index (Spanish)
│   │   └── iso_29148_labs_en.html # ISO 29148 index (English)
│   └── ISOIEC_25010_2023_Labs/
│       ├── iso_25010_labs.html    # ISO 25010 index (Spanish)
│       └── iso_25010_labs_en.html # ISO 25010 index (English)
└── Juegos/
    └── sqs_wp_players/
        ├── index.html            # Games hub
        ├── iso-index.html        # ISO Laboratory language selector
        ├── iso-real.html         # ISO simulator (Spanish)
        ├── iso-real-en.html      # ISO simulator (English)
        ├── simple-game.html      # Simplified mode
        ├── *.css                 # Stylesheets
        ├── *.js                  # Game engines
        └── proyecto-medcore/
            ├── medcore-enhanced-game.html    # MedCore (Spanish)
            ├── medcore-enhanced-game-en.html # MedCore (English)
            └── *.css                         # Project styles
```

## 🎮 Educational Games Included

### 1. **ISO Laboratory – Technical Decision Simulator**
- **File:** `Juegos/sqs_wp_players/iso-index.html`
- **Description:** Full simulator that teaches ISO standards through realistic software decisions.
- **Highlights:**
  - Four project archetypes (E-commerce, Hospital, FinTech, Social Network)
  - Eight ISO 25010 metrics tracked in real time
  - Resource management plus random events
  - Bilingual interactive quiz

### 2. **MedCore Hospital System**
- **Files:**
  - `Juegos/sqs_wp_players/proyecto-medcore/medcore-enhanced-game.html` (Spanish)
  - `Juegos/sqs_wp_players/proyecto-medcore/medcore-enhanced-game-en.html` (English)
- **Description:** Specialized simulator for hospital system development.
- **Highlights:**
  - Five full project phases
  - ISO 25010 metrics tailored to healthcare environments
  - Real-time dashboard
  - Visual alerting system

### 3. **Game Hub**
- **File:** `Juegos/sqs_wp_players/index.html`
- **Description:** Unified entry point for all games.
- **Highlights:**
  - Five-step interactive tutorial
  - Central scenario selector
  - XP progression with achievements
  - Global stats widget

## 🧪 Interactive Labs

### 1. ISO 9241 Labs – Ergonomics & Human-System Interaction
- **Key pages:** lab1_es.html, lab2_en.html, lab3_en.html, lab5_en.html, lab6_en.html
- **Highlights:**
  - Responsive professional layouts
  - Integrated navigation between labs
  - Full bilingual support
  - Detailed lists of educational materials per lab

### 2. ISO/IEC/IEEE 29148 Labs – Requirements Engineering
- **15 specialized labs:** Complete coverage of the standard.
- **Highlights:**
  - Elicitation and analysis (Labs 1–5)
  - Documentation and formalization (Labs 6–10)
  - Validation and verification (Labs 11–15)
  - Real case studies and practical exercises

### 3. ISO/IEC 25010:2023 Labs – Software Quality
- **10 quality labs:** Latest 2023 model.
- **Highlights:**
  - Functionality and performance (Labs 1–4)
  - Security and maintainability (Labs 5–8)
  - Usability and compatibility (Labs 9–10)
  - Innovations for AI/ML, cloud-native, and privacy-by-design contexts

## 🌐 External Links

### Cloud Apps
- **ISO Quiz:** https://sqswp035isoufvnew-y2xt6ew0.b4a.run/

### Educational GPTs
- **ExamGPT-UFV:** https://chatgpt.com/g/g-6909f37ba7388191a27b14a642d08d6c-examgpt-ufv
- **ConsultorLabISO-WP35-UFV:** https://chatgpt.com/g/g-6918a8d83fe48191990965457ee82e30-consultinglabiso-wp35-ufv
- **ISOQuest-UFV:** https://chatgpt.com/g/g-68beb9e2b1f88191b19935518a3e260c-isoquest-ufv

## 🚀 Usage Instructions

### Deploying on a Web Server
1. **Upload every file** to the server root.
2. **Set `index.html`** as the default page.
3. **Verify relative links** across all sections.
4. **Smoke-test navigation** between pages and games.

### Using Locally
1. **Open `index.html`** in a modern browser.
2. **Navigate between sections** via the main menu.
3. **Launch games** from the corresponding cards.
4. **Switch language** using the links on each page.

## 📋 ISO Standards Covered

- **ISO 9241:** Ergonomics of human-system interaction
- **ISO/IEC/IEEE 29148:** Requirements engineering
- **ISO/IEC 25010:2023:** Software product quality

## ✨ Technical Traits

- **🌐 Zero external dependencies:** All assets bundled
- **📱 Responsive design:** Works on mobile, tablet, and desktop
- **♿ Accessibility:** WCAG AA compliant layouts
- **⚡ High performance:** Optimized static assets
- **🔒 Safe:** Pure HTML/CSS/JavaScript, no back-end services

## 📝 Important Notes

- **🚫 Do not modify** the original core-project files
- **✅ Standalone:** This directory works entirely on its own
- **🔄 Updates:** Copy changes manually from the main project when needed
- **📧 Support:** Reach out to the development team for adjustments

---

**📅 Created:** 10 September 2025  
**🎯 Purpose:** Navigable documentation for public hosting  
**✅ Status:** Complete and production ready  