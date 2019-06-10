Week 11 assignment

Chapter 5



**p3**

| path    | y    | z    | w    | v    | u    | t    |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- |
| x       | 6    | 8    | 6    | 3    | inf  | inf  |
| xv      | 6    | 8    | 6    | 3    | 6, v | 7, v |
| xvyzxut | 6    | 8    | 6    | 3    | 6. v | 7, v |



**p6**

for the longest path, when the last node is reached, the algorithm must converge.



**p11**

a) the forwarding table at node x:

|      | x    | y    | z    | w    |      |
| :--- | ---- | ---- | ---- | ---- | ---- |
| x    | 0    | 4    | 6    | 5    |      |
| y    | 4    | 0    | 2    | 1    |      |
| z    | 5    | 1    | 0    | 1    |      |
| w    | 6    | 2    | 1    | 0    |      |

b) 

yes, there's x-y-z loop more than 2 nodes.

in my assumption nodes soon know x-y is 60. In the solution at t0 z tells y that z-x is 6 but that path is z-w-y-x so it should be ∞. Or does the node only identify the first node on its path? er, right, that's based on the forwarding table.

so for z, every 3 iterations brings 5+ for z-x, so when z-x is 50 it's the 27th iteration. then through this all values are finally clarified at 31st.

c)

y-x is infinity.



**p14**

eBGP, iBGP, e, i



**p19**

to b: aw, av

to c: av

baw, bav, av