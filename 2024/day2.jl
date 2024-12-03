lines = [parse.(Int, split(line)) for line in readlines("2024/input/input2")]

safe(v::Vector{Int}) = (v[1] > v[2] && v[end] < v[end-1]) ? safe(v[end:-1:1]) : all( x ∈ v[i-1]+1:v[i-1]+3 for (i, x) in collect(pairs(v))[2:end] )
safe2(v::Vector{Int}) = any(safe( [v[1:1:i-1]; v[i+1:1:end]] ) for i in 1:length(v) )

println(length(filter(safe, lines)))
println(length(filter(safe2, lines)))