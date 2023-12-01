# Working of list

## Advantages

- Random access
- Cache friendly

## Disadvantages

- Insertion, Deletion are slow
- Search is also slow for unsorted list

## How does dynamic size work?

- Preallocate some extra space
- If becomes full,
  - Allocate a new space for larger size(multiply by x)
  - Copy old space to new space
  - Free old space

## Note

---
Time complexity of list append is constant because it is appending at the end of the list, if you try to insert in the middle thats going to take linear time.
Similarly removing the last item using pop is also constant time complexity but removing other elements have linear time.

---

## Slicing(List,Tuple and String)

Slicing in Python is a feature that enables accessing parts of the sequence.

```python
l = [10,20,30,40,50]
print(l[0:5:2]) # Output - [10,30,50]
```

`sample_list[start:stop:step]` Gives a list with elements `sample_list[start], sample_list[start+step], sample_list[start+2*step]...` stop is not included.
