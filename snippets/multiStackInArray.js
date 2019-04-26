class MultiStack {
    constructor(nStacks) {
        //store all the combined values into a single array
        this.arr = [];
        //track the sizes of each stack 
        this.capacity = new Array(nStacks);
        //keep track of how many stacks are in the array
        this.nStacks = nStacks;
    }

    push(stackNum, value) {
        //check if stackNum exists 
        if (stackNum > this.nStacks)
            throw new Error("No such stack for specified stack number");

        //check if capacity for specified stackNum exists
        if (this.capacity[stackNum] == null || this.capacity[stackNum] < 0)
            this.capacity[stackNum] = 0;
        else 
            this.capacity[stackNum]++;
        
        //push into array
        this.arr[(this.capacity[stackNum]) * (this.nStacks) + stackNum] = value;
    }

    pop(stackNum) {
        //check if stackNum exists 
        if (stackNum > this.nStacks)
            throw new Error("No such stack for specified stack number");
        
        //check bounds
        if(this.capacity[stackNum] < 0)
            return; 

        //pop value
        let popped = this.arr[(this.capacity[stackNum]) * (this.nStacks) + stackNum];
        
        //delete from array
        delete this.arr[(this.capacity[stackNum]) * (this.nStacks) + stackNum];

        //decrement
        this.capacity[stackNum]--;

        return popped;
    }

    peek(stackNum) {
        //check if stackNum exists 
        if (stackNum > this.nStacks)
            throw new Error("No such stack for specified stack number");

        return  this.arr[(this.capacity[stackNum]) * (this.nStacks) + stackNum];
    }

    length(stackNum) {
        return this.capacity[stackNum];
    }

    isEmpty(stackNum) {
        //check if stackNum exists 
        if (stackNum > this.nStacks)
            throw new Error("No such stack for specified stack number");
        
        return (this.length(stackNum) <= 0) ?  true : false;
    }

    indexOfTop(stackNum) {
        //check if stackNum exists 
        if (stackNum > this.nStacks)
            throw new Error("No such stack for specified stack number");
        
        return (this.capacity[stackNum]) * (this.nStacks) + stackNum;
    }
}

let m = new MultiStack(1);

for (let i = 0; i < 10; i++) {
    m.push(i % 1, i);
}

console.log(m.arr);

for (let i = 0; i < 10; i++) {
    //console.log(m.pop(i % 1));
    console.log(m.indexOfTop(i%1));
}
console.log(m.arr);

