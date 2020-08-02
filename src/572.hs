-- | This is an implementation of the next permutation problem in Haskell for
-- fun
-- Given a number represented by a list of digits, find the next greater
-- permutation of a number, in terms of lexicographic ordering. If there is not
-- greater permutation possible, return the permutation with the lowest
-- value/ordering. For example, the list [1,2,3] should return [1,3,2]. The
-- list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].
-- Can you perform the operation without allocating extra memory (disregarding
-- the input memory)?
module NextPermutation where

import Data.List

-- | Generate a permutation of numbers using only the digits given in the
-- current list with the smallest lexicographical ordering that's higher than
-- the given number.
nextPermutation :: (Eq a, Ord a) => [a] -> [a]
nextPermutation [] = []
nextPermutation oldPerm =
  if pivotIndex == -1
    then -- If the pivotIndex is -1, that means we don't have an index to pivot
    -- on, which means that we've reached the last permutation, so we need to the
    -- sorted list, which is the first permutation
      sort oldPerm
    else prePivot ++ [swapVal] ++ swapWithPivot
  where
    pivotIndex = findPivotIndex $ enumerate oldPerm
    swapVal = undefined
    prePivot = take pivotIndex oldPerm
    swapWithPivot = []

-- | Find the index `i` such that `xs[i] < xs[i + 1]`. This method expects an
-- enumerated list of the form `[(idx, val), ...]`.
findPivotIndex :: (Ord a) => [(Int, a)] -> Int
findPivotIndex (x@(xIdx, xVal) : y@(yIdx, yVal) : rest) =
  if xVal < yVal
    then xIdx
    else findPivotIndex (y : rest)
findPivotIndex _ = -1

-- | Enumerate a list, in the style of python. This returns a tuple of elements
-- of the form `(index, elem)`.
enumerate = zip [0 ..]

-- | Find the minimum element in a list that's greater than some value
minGreaterThan :: (Bounded a, Ord a) => a -> [a] -> a
minGreaterThan greaterThan lst = go greaterThan maxBound lst
  where
    go greaterThan currMin [] = currMin
    go greaterThan currMin (x : xs) =
      if x < currMin
        then go greaterThan x xs
        else go greaterThan currMin xs

main = do
  putStrLn "Not implemented yet"
