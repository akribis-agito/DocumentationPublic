# Velocity control

The following block diagram shows the typical velocity control structure (including all the internal scaling).

![image58.png](../../../assets/image58.png)

The output of position loop (if present) will be summed with the scaled and filtered position derivative. The sum will pass through the dual loop scaling factor that compensates for the resolution differences between position and velocity feedback, if dual loop is used.

The scaled result, VelRef will subtract velocity feedback (Vel\[1\]), to produce velocity error (VelErr). VelErr will pass through PI controller, 4 customisable filters and output scaling to form velocity loop output.

The table below shows the summary of velocity control keywords.

| No. | Keywords     | Summary                                                  |
|-----|--------------|----------------------------------------------------------|
| 1   | dPosRefFilt  | Filter cutoff frequency of position reference derivative |
| 2   | VelGain      | Velocity loop proportional gain                          |
| 3   | VelKi        | Velocity loop integral gain                              |
| 4   | VelFiltOn    | Velocity loop filter switches                            |
| 5   | VelFiltDef   | Velocity loop filter definition parameters               |
| 6   | VelTrackFact | Scaling factor of filtered position reference derivative |
