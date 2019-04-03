//Backpack problem
function bp(backpackSize, items) {
  console.log(backpackSize);
  console.log(items);

  //solve subproblems
  let dp = new Array(backpackSize+1);
  for (let e = 0; e < dp.length; e++)
    dp[e] = new Array(items.length+1);

  for (let i = 0; i <= items.length; i++) {
    for (let j = 0; j < dp.length; j++) {
      if (i == 0 || j == 0){
        dp[i][j] = 0;
        continue;
      }
      let v = items[i-1].value;
      let w = items[i-1].weight;
      if(j<w)
        dp[i][j]=dp[i-1][j];
      else
        dp[i][j] = Math.max(v + dp[i - 1][j - w], dp[i - 1][j]);
    }
  }

  // backtrack to retrieve items picked
  let lifted = [];
  let curr=backpackSize;
  for(let i=items.length;i>0;--i){
    if(dp[i][curr]==dp[i-1][curr])
      continue;
    else {
      curr-=items[i-1].weight;
      lifted.push(items[i-1]);
    }
  }

  return lifted;
}

console.log(bp(10, [{
  "value": 1,
  "weight": 2
}, {
  "value": 2,
  "weight": 2
}, {
  "value": 3,
  "weight": 2
}, {
  "value": 7,
  "weight": 10
}]));
