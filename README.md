# GAZEBO dynamic simulation af abb irb 2600 

* Author: Ayman Damoun <damounayman@gmail.com>

dynamic simulation in gazebo of abb irb 2600 
## Table of Contents

> If your `README` has a lot of info, section headers might be nice.
- [About](#about)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Quick Start](#Quick Start)
- [License](#license)


---
## About
This work was carried out in the context of my research internship in the mixed laboratory between ENSAM and INRS.
The aim of the internship is to be able to simulate the emergency stop of a robot with sufficient precision to position the safety devices, in order to always check the safety distance between the operator and the robot.

---
## Dependencies

|             Dependency            | Version Tested On |
|:---------------------------------:|:-----------------:|
| [Gazebo](http://gazebosim.org/)   | 9.12.0            |
| [ROS](https://www.ros.org/)       | Melodic Morenia   |
| [Ubuntu](https://www.ubuntu.com/) | 18.04             |
---
## Installation

- First you need to install `ROS` and `GAZEBO` on your os. Check the `Dependencies`.

### Clone

- Clone this repo to your local machine using `https://github.com/damounayman/abb_irb2600_ws`

### Setup

- In a new terminal window 
```shell
$ cd abb_irb2600_ws
$ source devel/setup.bash
$ catkin_make
```
---
## Quick Start

![](./media/demo1.gif)

---
## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright .
