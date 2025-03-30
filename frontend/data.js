import { Sugg, Chai, Gopinath, Giraud } from "./user.js";

export class StepData {
  #dailyStepTotal = 0;
  #weeklyStepTotal = 0;
  #weeklyStepList = [0, 0, 0, 0, 0, 0, 0];
  #user;

  constructor(user) {
    this.#user = user;
  }

  updateDailyStepTotal(steps) {
    this.#dailyStepTotal = steps;
  }

  updateWeeklyStepTotal(steps) {
    this.#weeklyStepTotal = steps;
  }

  updateWeeklyStepListAll(list) {
    this.#weeklyStepList = list;
  }

  getDailyStepTotal() {
    return this.#dailyStepTotal;
  }

  getWeeklyStepList() {
    return this.#weeklyStepList;
  }

  getUser() {
    return this.#user;
  }
}

// Static test data for now
export const SuggData = new StepData(Sugg);
export const ChaiData = new StepData(Chai);
export const GopinathData = new StepData(Gopinath);
export const GiraudData = new StepData(Giraud);

// Example values
SuggData.updateDailyStepTotal(4345);
SuggData.updateWeeklyStepTotal(65669);
SuggData.updateWeeklyStepListAll([11020, 9033, 10221, 3441, 8933, 13003, 7567]);