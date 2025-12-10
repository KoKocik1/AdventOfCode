from collections import deque
from tqdm import tqdm

from pulp import LpMinimize, LpProblem, LpVariable, lpSum, value, PULP_CBC_CMD



class Indicator:
    result: list[str]
    buttons: list[list[int]]
    joltage: list[int]
    start_state: list[str]
    start_joltage: list[int]

    def __init__(self, result: list[str], buttons: list[list[int]], joltage: list[int]):
        self.result = result
        self.buttons = buttons
        self.joltage = joltage
        self.start_state = ['.'] * len(result)
        self.start_joltage = [0] * len(joltage)

    def switch_state(self, index: int, state: list[str]):
        if state[index] == '.':
            state[index] = '#'
        else:
            state[index] = '.'
        return state
    
    
    def find_state_bfs(self) -> int:
        queue = deque([(self.start_state, 0)])
        visited = {tuple(self.start_state)}
        
        while queue:
            current_state, counter = queue.popleft()
            
            for button in self.buttons:
                new_state = current_state.copy()
                for b in button:
                    new_state = self.switch_state(b, new_state)
                
                state_tuple = tuple(new_state)
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    if new_state == self.result:
                        return counter + 1
                    queue.append((new_state, counter + 1))
        
        return 0


    def find_joltage(self) -> tuple[dict[tuple[int, ...], int], int]:
        """
        Solve using Integer Linear Programming.
        
        Mathematical model:
        - Variables: x[j] = presses of button j (integer >= 0)
        - Constraints: For each position i: sum(x[j] where button j contains i) = joltage[i]
        - Objective: minimize sum(x[j])
        """
        
        # Create the optimization problem
        prob = LpProblem("Joltage_Minimization", LpMinimize)
        
        # Create variables: one for each button
        button_vars = {}
        button_tuples = [tuple(btn) for btn in self.buttons]
        
        # Upper bound: at most sum of all joltage values
        upper_bound = sum(self.joltage)
        
        for j, btn_tuple in enumerate(button_tuples):
            button_vars[btn_tuple] = LpVariable(
                f"x_{j}", 
                lowBound=0, 
                upBound=upper_bound, 
                cat='Integer'
            )
        
        # Objective: minimize total button presses
        prob += lpSum(button_vars.values()), "Total_Button_Presses"
        
        # Constraints: For each position i, sum of button presses must equal joltage[i]
        for i in range(len(self.joltage)):
            relevant_vars = []
            for btn_tuple in button_tuples:
                if i in btn_tuple:
                    relevant_vars.append(button_vars[btn_tuple])
            
            if relevant_vars:
                prob += lpSum(relevant_vars) == self.joltage[i], f"Position_{i}_Constraint"
        
        # Solve
        prob.solve(PULP_CBC_CMD(msg=0))
        
        if prob.status != 1:  # 1 = Optimal
            return None, 0
        
        # Extract solution
        solution = {}
        total_presses = 0
        for btn_tuple, var in button_vars.items():
            presses = int(value(var))
            if presses > 0:
                solution[btn_tuple] = presses
                total_presses += presses
        
        return solution, total_presses


class Indicators:
    indicators: list[Indicator]

    def __init__(self):
        self.indicators = []

    def find_states(self):
        count = 0
        for indicator in tqdm(self.indicators):
            count += indicator.find_state_bfs()
        return count

    def find_joltage(self):
        count = 0
        for indicator in tqdm(self.indicators):
            _, best_count = indicator.find_joltage()
            if best_count > 0:
                count += best_count
            else:
                print(f"Warning: No solution found for indicator")
        return count
