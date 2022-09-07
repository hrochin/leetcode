/**
 * @param {number[]} nums
 * @return {number[]}
 * @Description Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
 * Return the running sum of nums.
 */
var runningSum = function (nums) {
  let total = 0;

  let running_total = nums.map((num) => {
    total += num;
    return total;
  });
  return running_total;
};
