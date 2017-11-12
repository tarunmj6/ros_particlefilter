define sicklms ranger
(
  range_max 1.5
  sensor(
    fov 360.0
    samples 180
  )
  model
  (
    size [ 0.25 0.25 0.1 ]
    color "black"
  )
)

define robot position
(
  size [0.75 0.75 0.5]
  gui_nose 1
  drive "diff"
  name "robot" 
  color "red"
  sicklms(pose [ 0.0 0.000 0 0.000 ])
  velocity_bounds [-5.0 5.0 0 0 0 0 -90.0 90.0 ]
  acceleration_bounds [-5.0 5.0 0 0 0 0 -90 90.0 ]
)

define floorplan model
(
  color "gray30"
  boundary 1

  gui_nose 0
  gui_grid 0

  gui_outline 0
  gripper_return 0
  fiducial_return 0
  laser_return 1

  gui_move 0
)

resolution 0.02
interval_sim 100

