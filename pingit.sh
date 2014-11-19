#!/bin/bash

file="pingit-`date +%d-%m-%Y_%H-%M`.log"
echo "`date`\r\n" >> /var/log/pingit/$file

ping -c600  www.google.ch >> /var/log/pingit/$file
