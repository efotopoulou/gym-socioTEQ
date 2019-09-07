# gym-socioTEQ
OpenAI Gym Style SocioTEQ Environment.

Each observation includes four dimensions that represent:
* The percentage of positive interaction within the member of all the social sub-groups [range 0-100]  
** The overall members interaction is the sum of each participant positive interactions within the Action sub-group, multiplied by its reverse popularity   
* The Action Evaluation rate on behalf of all the participants [range 0-100]
* The Action Evaluation rate on behalf of the Group Facilitator [range 0-100]
* The Facilitaror evaluation on behalf of the Group Members [range 0-100]


```
observation [7, 15, 86, 28]
action 3
new observation [7.7, 16.5, 94.6, 30.8]
reward 37.4
done 0

```

# Requirement

* Python 3.5+
* OpenAI Gym
* NumPy

# Install
```
git clone https://github.com/efotopoulou/gym-socioTEQ.git
cd gym-socioTEQ/
pip install -e .
```
# Try example agents
```
cd examples/
python random_agent_SocioTEQEnv.py
```
