//Backpack problem
function bp(backpackSize, items) {
  console.log(items);
  //DP ARRAY
  let dp = new Array(backpackSize);
  for (let e = 0; e < dp.length; e++) {
    dp[e] = new Array(items.length);
  }
  //LIFTED
  let lifted = [];
  for (let i = 0; i < dp.length; i++) {
    for (let j = 0; j < items.length; j++) {
      let v = items[j].value;
      let w = items[j].weight;
      if (i == 0 || j == 0) dp[i][j] = 0;
      else dp[i][j] = Math.max([v + dp[i - 1][j - w], dp[i - 1][j]]);
    }
  }

  for (let i = 0; i < dp.length; i++) {
    for (let j = 0; j < dp[0].length; j++) {
      if (i >= 0 && j >= 1)
        if (dp[i][j] == dp[i][j - 1]) {
          lifted.push(items[j - 1]);
        }
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
  "value": 4,
  "weight": 10
}]));
