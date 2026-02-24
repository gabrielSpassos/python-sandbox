# AI Distillation POC

## What is?

Machine Learning technique, where a *simplier, smaller model (studant)* is trained to replicate the behavior of a *larger, more complex model (teacher)*, studant learns from the *teacher’s predictions* which contains richer information (often called soft targets).

The target is *retain most of teacher model's performance while reducing size, latency, and compute cost*

## How it works?

1. Train or obtain a powerful teacher model (large neural network, ensemble, or foundation model).
2. Run data through the teacher to produce probability distributions or outputs.
3. Train a student model to match those outputs (not just the correct label).
4. Deploy the smaller student model.

## Pros
- Smaller and faster
- Cheaper to deploy
- Often robust

## Cons
- Some accuracy loss is common
- Requires a strong teacher model
- Training pipeline becomes more complex

## Code

## Use Case

1. Edge and mobile deployment
    
    Large models often cannot run efficiently on phones, IoT devices, or embedded systems.

    Examples:

        - On-device speech recognition
        - Camera vision models
        - Offline translation apps

2. Large Language Model optimization

    Organizations distill large foundation models into smaller domain-specific ones.

    Examples:

        - Customer support chatbot distilled from a large LLM
        - Internal knowledge assistant
        - Coding assistant tuned for a specific language stack

    Benefits:

        - Faster responses 
        - Lower infrastructure cost
        - Better control and specialization

3. Production inference cost reduction

    At scale, inference cost dominates training cost.

    Companies distill:

        - Recommendation models
        - Fraud detection systems
        - Ranking models

    Result: same behavior, cheaper compute.

4. Privacy-sensitive deployments

    A large centralized model can train a smaller local model that runs without sending data to servers.

    Used in:

        - Healthcare tools
        - Enterprise on-prem systems
        - Personal devices

5. Ensemble compression

    Multiple models combined into one compact model.

    Example:

        - Replace a 10-model ensemble with a single distilled network
        - Keeps ensemble performance but simpler architecture

6. Domain adaptation

    Distill general intelligence into a specialized model.

    Examples:

        - Legal document classifier
        - Medical imaging detector
        - Financial risk analyzer

    The teacher provides broad knowledge; the student becomes efficient and specialized.

## Run POC

* Configure venv
```bash
python3 -m venv .venv
source .venv/bin/activate
```

* Install dependencies
```bash
pip3 install -r requirements.txt
```

* Run application
```bash
python3 main.py
```

## Output

```
Training teacher...
Teacher epoch 1, loss=191.656
Teacher epoch 2, loss=81.574
Teacher epoch 3, loss=56.448

Training student with distillation...
Student epoch 1, loss=1096.061
Student epoch 2, loss=267.952
Student epoch 3, loss=160.331

Evaluation:
Teacher accuracy: 97.62%
Student accuracy: 96.94%
```
