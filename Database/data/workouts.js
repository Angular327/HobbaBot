const mongoCollections = require('../config/mongoCollections');
const workouts = mongoCollections.workouts;

module.exports = {
    async getAllworkouts() {
        const workoutCollection = await workouts();
        const workoutList = await workoutCollection.find({}).toArray();
        if (!workoutList) throw 'No workouts in system!';
        return workoutList;
    },
    async getworkoutById(id) {
          const workoutCollection = await workouts();
          const workout = await workoutCollection.findOne({ _id: id });
          if (!workout) throw 'workout not found';
          return workout;
    },
    async addWorkout(UserID, User, Date){
        let newWorkout = {
            UserID: UserID,
            User: User,
            Date: Date,
        }
        let workoutCollection = await workouts();
        const insertInfo = await workoutCollection.insertOne(newWorkout);
        if(insertInfo.insertedCount === 0) throw 'Can not add workout';
        return true;
    },
}