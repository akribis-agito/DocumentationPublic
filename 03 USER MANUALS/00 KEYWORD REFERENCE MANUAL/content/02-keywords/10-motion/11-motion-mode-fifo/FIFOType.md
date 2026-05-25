# FIFOType

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

FIFO is a special motion mode in which the controller performs a sequence of linear and parabolic
segments, as defined by the user before the motion and optionally also during the motion.

The motion is created according to motion segments which are stored in a FIFO memory.

The motion segments definitions can be pushed to the FIFO at any time (before or during the
motion), providing that the FIFO is not full. If the FIFO is full, the push operation is rejected with a
suitable error.

If, during a motion in this mode, the controller reaches the last element in the FIFO, and
completing this motion segment, and yet no new element was pushed, the motion is automatically
ended.

The motion can be also stopped using the Stop or the StopFIFO functions. The first decelerate to
zero speed and the second makes the currently executed motion segment to be the last segment.

Each motion segment can be of type Velocity or Acceleration. Velocity type segment is a segment
in which the velocity reference is constant and Acceleration type segment is a segment in which
the acceleration reference is constant.

The time length of each segment (FIFOCycleTime) is a fixed value of number of control samples.
However, it can be modified at any time that the controller is ending a given segment and starting
a new one.

The FIFO is of size 512 entries. Each entry has type and value. See below for possible FIFO entry
types. If all entries are motion entries, the FIFO can hold up to 512 motion segments. Of course, it
can be re-filled over the communication, during the motion sequence.

The controller provides variety of parameters and functions to handle the FIFO and the motion
behavior, as described in details below.

Possible segment motions

            1. Velocity type motion segment:

                     a. Segment duration is known in number of samples (sample time of the control
                          loop). It is stored in the parameter FIFOCycleTime.

                     b. The segment starts naturally from the last position reference.
                     c. Motion definition can be given by one of:

                                i. Move linearly with given delta for position reference.
                                         1. Final target position is calculated using the given delta. The delta
                                              is given with scaling of the controller SAMPLING_FREQUENCY
                                              (typically 16384 Hz). This means that a delta of 1 [count] is

                                                                                                      Page 268

            Tel: +972-9-8909797 Fax: +972-9-8909796 email: info@agito.co.il website: www.agito.co.il
