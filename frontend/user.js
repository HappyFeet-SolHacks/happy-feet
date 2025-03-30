export class User {
    #name;
    #age;
    #dailyStepGoal;
    #weeklyStepGoal;
  
    constructor(name, age, dailyStepGoal, weeklyStepGoal) {
      this.#name = name;
      this.#age = age;
      this.#dailyStepGoal = dailyStepGoal;
      this.#weeklyStepGoal = weeklyStepGoal;
    }
  
    getDailyStepGoal() {
      return this.#dailyStepGoal;
    }
  
    getWeeklyStepGoal() {
      return this.#weeklyStepGoal;
    }
  
    setDailyStepGoal(goal) {
      this.#dailyStepGoal = goal;
    }
  
    setWeeklyStepGoal(goal) {
      this.#weeklyStepGoal = goal;
    }
  }
  
  // Static user instances
  export const Sugg = new User("Katie", 22, 10000, 70000);
  export const Chai = new User("Katie", 22, 10000, 70000);
  export const Gopinath = new User("Madhu", 20, 10000, 70000);
  export const Giraud = new User("Nalaya", 21, 10000, 70000);  