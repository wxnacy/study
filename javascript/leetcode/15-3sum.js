// 执行用时 : 280 ms, 在3Sum的JavaScript提交中击败了91.01% 的用户
// 内存消耗 : 46.7 MB, 在3Sum的JavaScript提交中击败了67.20% 的用户

var threeSum = function (nums) {
  let res = []
  let length = nums.length;
  nums.sort((a, b) => a - b) // 先排个队，最左边是最弱（小）的，最右边是最强(大)的
  // 同符号，则无解退出
  if( ( nums[0] < 0 && nums[length - 1] < 0 )
    || ( nums[0] > 0 && nums[length - 1] > 0 ) ) {
    return res
  }
  for (let i = 0; i < length - 2;) {
    if (nums[i] > 0) break; // 优化2: 最左值为正数则一定无解
    let first = i + 1
    let last = length - 1
    do {
      if (first >= last || nums[i] * nums[last] > 0) break // 两人选相遇，或者三人同符号，则退出
      let result = nums[i] + nums[first] + nums[last]
      if (result === 0) { // 如果可以组队
        res.push([nums[i], nums[first], nums[last]])
      }
      if (result <= 0 ) { // 实力太弱，把菜鸟那边右移一位
        while (first < last && nums[first] === nums[++first]){} // 如果相等就跳过
      } else { // 实力太强，把大神那边右移一位
        while (first < last && nums[last] === nums[--last]) {}
      }
    } while (first < last)
    while (nums[i] === nums[++i]) {}
  }
  return res
}


var res = threeSum([-1, 0, 1, 2, -1, -4])
console.log(res)
