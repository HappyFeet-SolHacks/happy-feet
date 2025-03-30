import { SuggData } from "./data.js";

document.addEventListener("DOMContentLoaded", () => {

    // populate content section
    const contentSection = document.querySelector(".content");
    if (!contentSection) {
        console.error("Element with class 'content' not found.");
        return;
    }


    // Create step graph div
    const stepGraph = document.createElement("div");
    stepGraph.classList.add("step-graph");

    // Ensure SuggData is defined
    if (!SuggData) {
        console.error("SuggData is undefined.");
        return;
    }

    // Get step data
    const weeklyStepList = SuggData.getWeeklyStepList();
    if (!weeklyStepList) {
        console.error("weeklyStepList is undefined.");
        return;
    }

    const maxSteps = Math.max(...weeklyStepList) || 1; // Avoid division by zero
    const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

    weeklyStepList.forEach((steps, index) => {
        const bar = document.createElement("div");
        bar.classList.add("bar");
        bar.style.height = `${(steps / maxSteps) * 100}%`;
        // bar.dataset.label = days[index];
        bar.dataset.value = steps;

        const label = document.createElement("span");
        label.classList.add("bar-label");
        label.textContent = `${days[index]}`;
        bar.appendChild(label);

        stepGraph.appendChild(bar);
    });

    contentSection.appendChild(stepGraph);
    console.log("Step graph added to content.");
});

document.addEventListener("DOMContentLoaded", () => {

    
    // Get DOM elements
    const progressCircle = document.querySelector(".progress-ring__circle");
    const progressText = document.querySelector(".progress-ring__text");
    const stepsLeftText = document.querySelector(".progress-ring__steps-left");

    // Get step data
    const dailyGoal = SuggData.getUser().getDailyStepGoal(); // Assuming this method exists
    const dailySteps = SuggData.getDailyStepTotal();
    const stepsRemaining = Math.max(dailyGoal - dailySteps, 0);

    // Update progress percentage
    const progressPercentage = (dailySteps / dailyGoal) * 100;
    const offset = 283 - (progressPercentage / 100) * 283; // Adjust stroke-dashoffset

    // Update SVG Circle
    progressCircle.style.strokeDashoffset = offset;
    progressText.textContent = `${Math.round(progressPercentage)}%`;
    stepsLeftText.textContent = `${stepsRemaining} left`;

    console.log(`Daily Steps: ${dailySteps}, Goal: ${dailyGoal}, Remaining: ${stepsRemaining}`);
});

