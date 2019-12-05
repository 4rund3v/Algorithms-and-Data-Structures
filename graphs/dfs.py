"""
dfs(g,r)
c ← new array(g.n)
dfs(g,r, c)
dfs(g,i, c)
c[i] ← grey
for j in g.out edges(i) do
if c[j] = white then
c[j] ← grey
dfs(g,j, c)
c[i] ← black"""
