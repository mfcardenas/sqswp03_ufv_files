export function calculateScore(scenario, answers) {
    if (!scenario) {
        return { total: 0, correct: 0, totalQuestions: 0, labs: [] };
    }

    let totalQuestions = 0;
    let correct = 0;

    scenario.challenges.forEach((challenge) => {
        (challenge.quizzes || []).forEach((quiz) => {
            totalQuestions += 1;
            const userAnswer = answers?.[challenge.id]?.[quiz.id];
            if (userAnswer !== undefined && userAnswer === quiz.answer) {
                correct += 1;
            }
        });
    });

    const percentage = totalQuestions === 0 ? 0 : Math.round((correct / totalQuestions) * 100);

    const labs = scenario.labs.map((lab) => {
        const labChallengeIds = new Set(lab.challengeIds);
        let labTotal = 0;
        let labCorrect = 0;
        scenario.challenges
            .filter((challenge) => labChallengeIds.has(challenge.id))
            .forEach((challenge) => {
                (challenge.quizzes || []).forEach((quiz) => {
                    labTotal += 1;
                    const userAnswer = answers?.[challenge.id]?.[quiz.id];
                    if (userAnswer !== undefined && userAnswer === quiz.answer) {
                        labCorrect += 1;
                    }
                });
            });
        return {
            labId: lab.id,
            title: lab.title,
            score: labTotal === 0 ? 0 : Math.round((labCorrect / labTotal) * 100),
            correct: labCorrect,
            total: labTotal
        };
    });

    return {
        total: percentage,
        correct,
        totalQuestions,
        labs
    };
}
