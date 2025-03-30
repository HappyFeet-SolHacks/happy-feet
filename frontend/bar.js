import { SuggData } from "./data.js";

document.addEventListener("DOMContentLoaded", () => {
  // ========== Bar Graph ==========
  const container = document.querySelector(".bar-graph-container");
  const stepGraph = document.createElement("div");
  stepGraph.classList.add("step-graph");

  const stepData = SuggData.getWeeklyStepList();
  const maxSteps = Math.max(...stepData, 1);
  const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

  stepData.forEach((steps, i) => {
    const bar = document.createElement("div");
    bar.classList.add("bar");
    bar.dataset.label = days[i];
    bar.dataset.value = steps;
    bar.style.height = `${(steps / maxSteps) * 100}%`;
    stepGraph.appendChild(bar);
  });

  container.appendChild(stepGraph);

  // ========== Circular Progress Ring ==========
  const progressCircle = document.querySelector(".progress-ring__circle");
  const progressText = document.querySelector(".progress-ring__text");
  const stepsLeftText = document.querySelector(".progress-ring__steps-left");

  const dailyGoal = SuggData.getUser().getDailyStepGoal();
  const stepsToday = SuggData.getDailyStepTotal();
  const remaining = Math.max(dailyGoal - stepsToday, 0);
  const percentage = (stepsToday / dailyGoal) * 100;
  const dashoffset = 283 - (percentage / 100) * 283;

  progressCircle.style.strokeDashoffset = dashoffset;
  progressText.textContent = `${Math.round(percentage)}%`;
  stepsLeftText.textContent = `${remaining} left`;
});

