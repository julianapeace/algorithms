/*
https://www.khanacademy.org/computing/computer-science/algorithms/sorting-algorithms/p/challenge-implement-swap

  */
var swap = function(array, firstIndex, secondIndex) {
  let temp = array[firstIndex];
	array[firstIndex] = array[secondIndex];
	array[secondIndex] = temp;
};

var testArray = [7, 9, 4];
swap(testArray, 0, 1);

console.log(testArray);
