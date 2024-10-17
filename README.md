### Simulation Concept

The simulation aims to answer a certain question: How many generations of people does it take for every one of the k original families to be within everyone in the living population.
$k =$ amount of every original family, $1 <= k$.

### Rules

Every couple has 2 children a male and a female child.

<ul>A person can procreate with another person if:
    <li>Both people have not procreated again</li>
    <li>If they are not the same gender</li>
</ul>

The "chaser" selects their partner based on how distant of a a relative they are.

The simulation ends when in a generation, every person is a relative of every starting family.

### Results

### Failed algorithms

I had different rules on how the couples were picked in the beginning. The rules originally were:

The "chaser" chooses a partner if they are not relatives or if they are distant relatives.

For this I used a basic search algorithm and after a backtracking algorithm but this approach did not work.
(can be seen in _old files)