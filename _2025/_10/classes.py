from collections import deque
from itertools import combinations_with_replacement
from collections import Counter


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
            
    def find_state(self) -> int:
        queue = deque([(self.start_state, 0, [])])
        while queue:
            current_state, counter, history = queue.popleft()
            counter += 1
            for button in self.buttons:
                new_state = current_state.copy()
                for b in button:
                    new_state = self.switch_state(b, new_state)
                new_history = history + [button]
                queue.append((new_state, counter, new_history))
                if new_state == self.result:
                    return counter
    
    def _find_all_buttons(self, idx: int) -> list[list[int]]:
        buttons = []
        for button in self.buttons:
            if idx in button:
                buttons.append(button)
        return buttons

    def _find_all_combinations(self, buttons: list[list[int]], joltage: int) -> list[dict[tuple[int, ...], int]]:
        combos = combinations_with_replacement(map(tuple, buttons), joltage)

        result = []
        for combo in combos:
            dict_combo = dict(Counter(combo))
            if self._check_occurence(dict_combo):
                result.append(dict_combo)
        
        return result

    def _check_occurence(self, dict_combo: dict[tuple[int, ...], int]) -> bool:
        dict_occurence = {}
        for idx in range(len(self.joltage)):
            dict_occurence[idx] = 0
            
        for button, count in dict_combo.items():
            for b in button:
                dict_occurence[b] += count

        for idx, count in dict_occurence.items():
            if count > self.joltage[idx]:
                return False
        return True

    def _check_combination(
        self,
        combination: dict[tuple[int, ...], int],
        combination_dict: dict[int, dict[tuple[int, ...], int]],
        # final_dict: dict[tuple[int, ...], int]
    ) -> bool:
        final_combination_dict = []
        for idx in range(len(combination_dict)):
            current_combination = combination_dict[idx]
            include = True
            # here check
            for button, count in current_combination.items():
                if button in combination:
                    if count < combination[button]:
                        include = False
                        break
            if include:
                new_dict = current_combination.copy()
                for button, count in combination.items():
                    if button not in new_dict:
                        new_dict[button] = count
                if self._check_occurence(new_dict):
                    final_combination_dict.append(new_dict)
        return final_combination_dict

    def find_joltage(self) -> int:
        combination_dict = {}
        possible_combinations = []
        for idx, joltage in enumerate(self.joltage):
            buttons = self._find_all_buttons(idx)
            all_combinations = self._find_all_combinations(buttons, joltage)
            combination_dict[idx] = all_combinations
            possible_combinations.extend(all_combinations)
        
        final_dict = combination_dict[0]
        for idx in range(1, len(self.joltage)):
            new_final_dict = []
            for c in combination_dict[idx]:
                new_final_dict.extend(self._check_combination(
                        c, final_dict))
            final_dict = new_final_dict
                # new_possible_combinations = []
                # for combination in possible_combinations:
                #     for all_combination in all_combinations:
                #         if all_combination in combination:
                #     if combination in combination_dict[idx-1]:
                #         possible_combinations.remove(combination)
        best_dict = None
        best_count = 0
        for f in final_dict:
            count = 0
            for button, c in f.items():
                count += c
            if best_count==0 or count < best_count:
                best_dict = f
                best_count = count

        return best_dict, best_count
        
        
        
        print("1")
        # queue = deque([(self.start_joltage, 0, [])])
        # while queue:
        #     current_state, counter, history = queue.popleft()
        #     counter += 1
        #     for button in self.buttons:
        #         new_state = current_state.copy()
        #         for b in button:
        #             new_state = self.switch_state(b, new_state)
        #         new_history = history + [button]
        #         queue.append((new_state, counter, new_history))
        #         if new_state == self.result:
        #             return counter
            
            
                

class Indicators:
    indicators: list[Indicator]

    def __init__(self):
        self.indicators = []
        
    def find_states(self):
        count=0
        for indicator in self.indicators:
            count += indicator.find_state()
        return count

    def find_joltage(self):
        count=0
        for indicator in self.indicators:
            best_dict, best_count = indicator.find_joltage()
            print(best_dict, best_count)
            count += best_count
        return count
