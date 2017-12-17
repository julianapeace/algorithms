"""
https://www.hackerrank.com/challenges/itertools-permutations/problem
Submitted 12120 times

INPUT:

HACK 2

OR:

PQRST 4
"""
from itertools import permutations

def make_permutation(string, size):
    ans = list(permutations(string,size))
    for i in range(0, len(ans)):
        print("".join(ans[i]))

if __name__ == "__main__":
    a = input().strip().split()
    string = sorted(list(a[0]))
    size = int(a[1])
    make_permutation(string, size)

"""
API-KEY=2ca47b125d83d46bd601b0c08245152ec8c07d51
TO CREATE CUSTOM MODEL:
curl -X POST \
--form "beagle_positive_examples=@beagle.zip" \
--form "husky_positive_examples=@husky.zip" \
--form "goldenretriever_positive_examples=@golden-retriever.zip" \
--form "negative_examples=@cats.zip" \
--form "name=dogs" \
"https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key={api-key}&version=2016-05-20"

TO TRAIN AN EXISTING MODEL:
curl -X POST \
--form "dalmatian_positive_examples=@dalmatian.zip" \
--form "negative_examples=@more-cats.zip" \
"https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers/dogs_1411545191?api_key=2ca47b125d83d46bd601b0c08245152ec8c07d51&version=2016-05-20"

TO CHECK STATUS OF TRAINING:
curl -X GET \
"https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers/{classifier_id}?api_key={api-key}&version=2016-05-20"

"""
