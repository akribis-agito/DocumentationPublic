# Pre-cruise

Pre-cruise is an optional first stage of a sine point-to-point move in which the axis travels a defined opening stretch at a higher speed before slowing to the normal cruise speed for the rest of the move.

These keywords apply to the sine point-to-point motion modes added in v5: [MotionMode](../02-motion-configuration/MotionMode.md) `= 20` (sine PTP) and `= 21` (sine PTP repetitive). **The pre-cruise feature, and these keywords, are central-i v5 only.**

## What pre-cruise is for

In an ordinary point-to-point move the axis accelerates to a single cruise speed ([Speed](../03-kinematics-configuration/Speed.md)), holds it, then decelerates to the target. A pre-cruise inserts an earlier, faster stage: the axis first accelerates to a higher **pre-cruise speed** ([PreCruiseSpd](PreCruiseSpd.md)), holds it across an opening stretch (the **pre-cruise stroke**), then drops back down to the cruise speed for the remainder of the move and finally decelerates to the target. It lets you cover the first part of a long move quickly and then approach the destination at a calmer, more controlled speed.

The pre-cruise stroke is the distance from the start of the move to the **pre-cruise target**, set either absolutely with [PreCruAbsTrgt](PreCruAbsTrgt.md) or as a distance with [PreCruRelTrgt](PreCruRelTrgt.md). The final destination is still the usual [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) of the sine point-to-point move.

![Pre-cruise speed-vs-time stages](pre-cruise-timeline.svg)

## How the stages compose

A move with pre-cruise runs as up to five sine-shaped stages:

1. accelerate from rest to the pre-cruise speed,
2. hold the pre-cruise speed,
3. decelerate from the pre-cruise speed down to the cruise speed,
4. hold the cruise speed,
5. decelerate to rest at the target.

A pre-cruise is only inserted when **both** of these hold:

- the pre-cruise speed is **greater than** the cruise speed (`PreCruiseSpd` &gt; `Speed`) — otherwise there is nothing higher to run first, and the move reduces to an ordinary sine point-to-point profile (stages 1, 4, 5); and
- a pre-cruise stroke is defined (a non-zero pre-cruise target).

## Conditions and rejections

When `Begin` is issued the controller checks the geometry before starting. If a condition is not met the move is rejected with an instruction error rather than being silently clipped:

| Condition | Effect if it fails |
|---|---|
| Total stroke and pre-cruise stroke point in the same direction | rejected — pre-cruise target must lie on the way to the final target (error 381) |
| Total stroke is longer than the pre-cruise stroke | rejected — the final target must be beyond the pre-cruise target (error 383) |
| Pre-cruise stroke is long enough to reach the pre-cruise speed and slow back to cruise speed | rejected — pre-cruise stroke insufficient (error 384) |
| Remaining stroke is long enough to decelerate to rest | rejected — stopping stroke insufficient (error 385) |

See the [instruction error codes](../../../04-error-codes/instruction-error-codes.md) page for the meaning of instruction error codes returned by `Begin`.

## Keywords in this category

| Keyword | Summary |
|---|---|
| [PreCruAbsTrgt](PreCruAbsTrgt.md) | Absolute position of the pre-cruise target (user units). |
| [PreCruRelTrgt](PreCruRelTrgt.md) | Pre-cruise target as a distance from the start of the move (user units). |
| [PreCruiseSpd](PreCruiseSpd.md) | Speed held during the pre-cruise stage. |

## See also

- [MotionMode](../02-motion-configuration/MotionMode.md) — modes 20 and 21 select sine point-to-point motion
- [Speed](../03-kinematics-configuration/Speed.md) — the cruise speed used after the pre-cruise stage
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — the final target of the move
- [Begin](../04-motion-command/Begin.md) — validates the geometry and starts the move
