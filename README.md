[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18893396&assignment_repo_type=AssignmentRepo)
# Algoritmen Oefening 4

Gegeven is een lijst genaamd nums met lengte n en een integer (geheel getal) genaamd target. Bepaal het aantal paren (i, j) waarvoor nums[i] + nums[j] < target.
De functie moet de naam countTargetPairs() krijgen.

Hierbij zijn i en j verschillend van elkaar en 0 <= i < n en 0 <= j < n.

Voorbeeld 1:

Invoer: nums = [-1,1,2,3,1], target = 2

Uitvoer: 3

Uitleg: Er zijn 3 paren van indices die voldoen aan de voorwaarden in de uitspraak:

(0, 1) aangezien 0 < 1 en nums[0] + nums[1] = 0 < target

(0, 2) aangezien 0 < 2 en nums[0] + nums[2] = 1 < target

(0, 4) aangezien 0 < 4 en nums[0] + nums[4] = 0 < target

Let op, (0, 3) wordt niet meegerekend omdat nums[0] + nums[3] niet strikt kleiner is dan het target.

Voorbeeld 2:

Invoer: nums = [-6,2,5,-2,-7,-1,3], target = -2

Uitvoer: 10

Uitleg: Er zijn 10 paren van indices die voldoen aan de voorwaarden in de uitspraak:

(0, 1) aangezien 0 < 1 en nums[0] + nums[1] = -4 < target

(0, 3) aangezien 0 < 3 en nums[0] + nums[3] = -8 < target

(0, 4) aangezien 0 < 4 en nums[0] + nums[4] = -13 < target

(0, 5) aangezien 0 < 5 en nums[0] + nums[5] = -7 < target

(0, 6) aangezien 0 < 6 en nums[0] + nums[6] = -3 < target

(1, 4) aangezien 1 < 4 en nums[1] + nums[4] = -5 < target

(3, 4) aangezien 3 < 4 en nums[3] + nums[4] = -9 < target

(3, 5) aangezien 3 < 5 en nums[3] + nums[5] = -3 < target

(4, 5) aangezien 4 < 5 en nums[4] + nums[5] = -8 < target

(4, 6) aangezien 4 < 6 en nums[4] + nums[6] = -4 < target
