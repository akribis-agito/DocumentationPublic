# RecTrigForce

**Definition:**

RecTrigForce will overrule the trigger detection and force the recording to continue. Forced trigger will occur regardless of whether RecTrigForce is called while pre-trigger data is filled, or while the scope is waiting trigger (after filling pre-trigger data).

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

For example, RecTrigForce\[1\] will force-trigger the first scope.

<span class="anchor" id="_RecTrigMask"></span>
