from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    
    answer = 0
    bridge_weight = 0
    while truck or bridge:
        bridge_weight -= bridge.popleft()
        
        if truck:
            if bridge_weight + truck[0] <= weight:
                bridge_weight += truck[0]
                bridge.append(truck.popleft())
            else:
                bridge.append(0)
        
        answer += 1
    
    return answer