using LinearAlgebra

filepath = "2024/input/input1"
l = countlines(filepath)
v1, v2 = zeros(Int64, l), zeros(Int64, l)
i = 0

for line in readlines(open(filepath))
    global i += 1
    v1[i], v2[i] = map((x) -> parse(Int, x), split(line, "   "))
end

p1sol = Int(norm(sort(v1)-sort(v2), 1))

p2sol = 0
for num in v1
    global p2sol += num * length(filter( (x)-> x==num, v2))
end

print("Part 1 solution: $p1sol")
print("Part 2 solution: $p2sol")