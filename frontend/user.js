export class User {
    #name;
    #age;
    #dailyStepGoal;
    #weeklyStepGoal;

    // In the future get user info from backend
    constructor(name, age, dailyStepGoal, weeklyStepGoal){
        this.#name = name;
        this.#age = age;
        this.#dailyStepGoal = dailyStepGoal;
        this.#weeklyStepGoal = weeklyStepGoal;
    }

    setDailyStepGoal(int){
        this.#dailyStepGoal = int
    }

    getDailyStepGoal(){
        return this.#dailyStepGoal
    }

    setWeeklyStepGoal(int){
        this.#weeklyStepGoal = int
    }

    getWeeklyStepGoal(){
        return this.#weeklyStepGoal
    }
}

// create static users
export const Sugg = new User("Katie", 22, 10000, 70000);
export const Chai = new User("Katie", 22, 10000, 70000);
export const Gopinath = new User("Madhu", 20, 10000, 70000);
export const Giraud = new User("Nalaya", 21, 10000, 70000);
