from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, AutoScaling
from diagrams.aws.network import PrivateSubnet, ELB

with Diagram("Infraestrutura final RabbitMQ", show=False, direction="LR"):

    with Cluster("VPC"):
        elb = ELB("Load Balancer")
        asg = AutoScaling("Auto Scaling Group")
        
        with Cluster("Zona A"):  
            ec2_az1 = EC2("Instância EC2")
        
        with Cluster("Zona B"):  
            ec2_az2 = EC2("Instância EC2")
        
        elb >> asg
        
        asg - ec2_az1
        asg - ec2_az2
