//author: Cytron team

let RIDES = [] // list of rides
let VEHICLES = [] //list of cars in order of the next to select a ride
let startRide = [
]

//READ INPUT
const fs = require("fs")
let input = fs.readFileSync("./input").toString().split("\n")

const [ROW,COLUMN,FLEET,RIDE_NUM,BONUS,STEPS] = input[0].split(" ").map(st=>parseInt(st))

for (let i = 1; i<= RIDE_NUM; i++){
startRide.push(input[i].split(" ").map(str=>parseInt(str)))
}


createVehicle(FLEET)
console.log(VEHICLES.length,RIDE_NUM)

input.slice(1).forEach((ride_str, i) => {
    let ride = input[i].split(" ").map(str=>parseInt(str))
    RIDES.push(createRide(ride[0], ride[1], ride[2], ride[3], ride[4], ride[5], i))
})

AssignRide()
// console.log(VEHICLES)

fs.writeFileSync("ouput_b.out",output())

function output(){
    let str = ""
    VEHICLES.forEach((vec,i)=>{
        str += `${vec.rides.length} ${vec.rides.join(" ")}\n`
    })
    return str
}



function AssignRide() {
    let len = RIDES.length
    const rides = [...RIDES]
    while (rides.length) {
        debateOnRide(rides)
    }
}

function debateOnRide(rides) {
    console.log("hello brov")
    let usedVec = [],
        obj = {};
    let scale = []

    VEHICLES.forEach((vehicle, i) => {
        let r = rides.map(ride => {
            return {
                index: ride.index,
                score: scoreRide4Vehicle(vehicle, ride)
            }
        })
        r.forEach(j => {
            scale.push({
                score: j.score,
                index: j.index,
                vecIndex: i
            })
        })
    })

    scale.sort((a, b) => b.score > a.score)

    let minLen = Math.min(rides.length, VEHICLES.length)
    for (let j = 0; j < minLen; j++) {
        // console.log(scale)
        let {
            score,
            index,
            vecIndex
        } = scale.shift()
        scale = scale.filter((s, i) => {
            return !(s.index == index || s.vecIndex == vecIndex)
        })

        let rIndex = rides.indexOf(RIDES[index])
        rides.splice(rIndex, 1)
        if (score){
             VEHICLES[vecIndex].rides.push(index)
        }
       
        VEHICLES[vecIndex].currentStep = getB4End(VEHICLES[vecIndex], RIDES[index])
        VEHICLES[vecIndex].currentIntersection = RIDES[index].finishIntersection
    }


}

function getDistance(start, end) {
    return Math.abs(start[0] - end[0]) + Math.abs(start[1] - end[1])
}

function createVehicle(num) {
    for (let i = 0; i < num; i++) {
        VEHICLES.push({
            currentStep: 0,
            rides: [],
            currentIntersection: [0, 0]
        })
    }
}

//creates a ride from ride values
function createRide(a, b, x, y, s, f, i) {
    return {
        startIntersection: [a, b],
        finishIntersection: [x, y],
        earliestStart: s,
        latestFinish: f,
        index: i
    }
}

function canGetThereOnTime(v, r) {
    const getThereBy = v.currentStep + getDistance(v.currentIntersection, r.startIntersection)
    if (getThereBy <= r.earliestStart) {
        return BONUS
    }
    return 0
}

function canFinishOnTime(v, r) {
    if (getB4End(v, r) <= r.latestFinish) {
        return getDistance(r.startIntersection, r.finishIntersection)
    }
    return 0
}

function b4TRunsOut(v, r) {
    // console.log(v,r,getB4End(v,r))
    if (( getB4End(v, r)) > STEPS) {
        return 0
    }
    return 1
}

function getB4End(v, r) {
    const getThereBy = v.currentStep + getDistance(v.currentIntersection, r.startIntersection)
    return getThereBy + getDistance(r.startIntersection, r.finishIntersection)
}

function scoreRide4Vehicle(v, r) {
    return b4TRunsOut(v, r) * (canFinishOnTime(v, r) + canGetThereOnTime(v, r))
}



function sortRideByVehicle(v, r) {
    const rides = r
    return rides.sort((a, b) => scoreRide4Vehicle(v, a) < scoreRide4Vehicle(v, b))
        .map(ride => ({
            index: ride.index,
            score: scoreRide4Vehicle(v, ride)
        }))
}
