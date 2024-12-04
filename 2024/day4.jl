using LinearAlgebra # for the diag function
data = reshape(filter( (x) -> x != '\n', collect(Char, read("2024/input/input4"))), (:, countlines("2024/input/input4")))


pt1 = sum(length(collect(eachmatch(r"(XMAS|SAMX)", String(s), overlap=true))) # Regex 
            for s in vcat( # applied to each 
                eachcol(data), # column 
                eachrow(data), # row
                [diag(data, i) for i in -size(data)[1]+1:size(data)[2]-1], # diagonal
                [diag(reverse(data, dims=1), i) for i in -size(reverse(data, dims=1))[1]+1:size(reverse(data, dims=1))[2]-1])); # reverse diagonal

isx_mas(m) = return all(ss ∈ ["SAM", "MAS"] for ss in String.(diag.([m, reverse(m, dims=1)]))) # takes in 3x3 matrix and returns if its diagonals are both MAS
submatrices(d, n) = [d[i:i+n-1,j:j+n-1] for i in 1:(size(d)[1]+1-n) for j in 1:(size(d)[2]+1-n)] # Returns all 3x3 submatrices of data

pt2 = length(filter(isx_mas, submatrices(data, 3)));

println("Part 1 Solution: $pt1")
print("Part 2 Solution: $pt2")