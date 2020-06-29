echo "Starting the Gazebo simulation of irb2600"

gnome-terminal -x sh -c "roslaunch abb_irb2600_gazebo irb2600_12_165_gazebo.launch; exit"

sleep 10

echo "Starting Moveit and Rviz"

gnome-terminal -x sh -c "roslaunch abb_irb2600_moveit_config abb_irb2600_planning_execution.launch; exit"
