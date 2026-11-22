#! /usr/bin/env python3
# ensures that the first python 3 is usein your system is usein
# called the shebang lline

"""
Description:
    This ROS 2 node periodically publishes "Hello World" messages to a topic.

------ 
Publishing Topics:
    The channel containing the "Hello World" messages 
    /py_example/topic - std_msgs/String

Subscription Topics:
    None
------ 
Author: Addison Sears-Collins
Date: April 4, 2025
"""
import rclpy # Import the ROS 2 client library for python
from rclpy.node import Node # Import the node class, used for creating nodes 

from std_msgs.msg import String # Import string message types 

class MinimalPyPublisher(Node):
    """ Create a minimal publisher node class for publishing messages

    """

    def __init__(self):
        """
        Create a custom node class for publishing messages
        """
        # Initialize the node with a name 
        super().__init__('minimal_py_publisher')

        # Create a publishder on the topic with a queue size of 10 messages  
        self.publisher_1 = self.create_publisher(String, "/py_example_topic", 10)

        # Create a timer with a period of 0.5 seconds to trigger publishing a message
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Initialize a counter variable for message content
        self.i = 0

    def timer_callback(self):
        """Callback function executed periodically by the timer 
        """
        # Create a new String message object
        msg = String()

        # Set the messge data with a counter
        msg.data = f"Hello World: {self.i}"

        # Publish the message you created above to a topic (publisher)
        self.publisher_1.publish(msg);

        # Log a message indicating the message has been publisher
        self.get_logger().info(f'Publishing: {msg.data}')

        self.i += 1;

def main(args=None): 
    """Main function to start the ROS 2 node

    Args:
        args (List, optional): Command-line arguments. Defaults to None
    """
    rclpy.init(args=args)

    # Create an instance of the minimal Publisher node 
    minimal_py_publisher = MinimalPyPublisher()

    rclpy.spin(minimal_py_publisher) # without this the program exits immediately

    # Destroy the node explicity
    minimal_py_publisher.destroy_node()

    # Shutdown ROS2 communication
    rclpy.shutdown()

if __name__ == '__main__':
    # Execute the main function if the script is run directly
    main()

