import { Sugg, Chai, Gopinath, Giraud } from "./user.js";

export class StepData {
    #dailyStepTotal;
    #isDailyGoal;
    #weeklyStepTotal;
    #isWeeklyGoal;
    #weeklyStepList;
    #user
    // #day

    // Construct data from backend in the future
    constructor(User){
        this.#dailyStepTotal = 0;
        this.#isDailyGoal = false;
        this.#weeklyStepTotal = 0;
        this.#isWeeklyGoal = false;
        this.#weeklyStepList = [0, 0, 0, 0, 0, 0, 0]
        this.#user = User
        // this.#day = 
    }

    dailyGoalReached(){
        this.#dailyStepTotal >= this.#user.getDailyStepGoal() ? this.#isDailyGoal = true : this.#isDailyGoal = false
    }

    weeklyGoalReached(){
        this.#weeklyStepTotal >= this.#user.getWeeklyStepGoal() ? this.#isWeeklyGoal = true : this.#isWeeklyGoal = false

    }

    updateDailyStepTotal(int){
        this.#dailyStepTotal = int
        this.dailyGoalReached()
    }

    updateWeeklyStepTotal(int){
        this.#weeklyStepTotal = int
        this.weeklyGoalReached()
    }

    updateWeeklyStepList(day, int){
        this.#weeklyStepList[converter(day)] = int
    }

    updateWeeklyStepListAll(list){
        this.#weeklyStepList = list
    }

    converter(string){
        if (string == "Sunday"){
            return 0
        } else if (string == "Monday"){
            return 1
        } else if (string == "Tuesday"){
            return 2
        } else if (string == "Wednesday"){
            return 3
        } else if (string == "Thursday"){
            return 4
        } else if (string == "Friday"){
            return 5
        } else if (string == "Saturday"){
            return 6
        } 
    }

    getWeeklyStepList() {
        return this.#weeklyStepList;
    }

}

// static users
export const SuggData = new StepData(Sugg);
export const ChaiData = new StepData(Chai);
export const GopinathData = new StepData(Gopinath);
export const GiraudData = new StepData(Giraud);

//It is Saturday
SuggData.updateDailyStepTotal(4345)
SuggData.updateWeeklyStepTotal(65669)
SuggData.updateWeeklyStepListAll([11020, 9033, 10221, 3441, 8933, 13003, 7567])
