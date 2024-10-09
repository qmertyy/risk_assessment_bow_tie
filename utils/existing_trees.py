class base_trees():
        def __init__(self,):
                self.base_software_failure_tree = {            
                                                'tree1': ( 'software_failure', ['programming', 'random_breakdown', 'hacking'], 'or'),        
                                        
                                        }       
                self.base_human_failure_tree = {            
                                                'tree1': ( 'human_error', ['limited_capabilities', 'external_factors'], 'or'),      
                                                'tree2': ('external_factors', ['accident', 'alcohol', 'distraction', 'asleep', 'stress'], 'or'),  
                                        
                                        }
                self.base_ais_failure_tree = {            
                                        'tree1': ( 'ais_failure', ['ais_hardware_failure', 'external_failure'], 'or'),         
                                        'tree2': ('ais_hardware_failure', ['receiver_failure', 'rf_antenna_failure'], 'or'),
                                        'tree3': ('external_failure', ['signal_jamming', 'incorrect_data_from_ts', 'ais_data_not_sent'], 'or'),
                                        'tree4': ('ais_data_not_sent', ['ais_hardware_failure', 'human_error'], 'or'),
                                        'tree5': ('human_error', [], 'transfer')
                                }

                self.base_hardware_failure_tree = {            
                                        'tree1': ( 'hardware_failure', ['pc_failure', 'random_breakdown'], 'or'),        
                                
                                }

                         
                self.base_bridge_network_failure_tree = {            
                                'tree1': ( 'bridge_network_failure', ['pc_failure', 'software_failure', 'clock_error'], 'or'),        
                               
                                
                                'tree7': ('software_failure', [], 'transfer'), 
                                #'tree8': ('clock_error', [], 'transfer'), 
                        }
                self.base_cctv_camera_failure_tree = {            
                                        'tree1': ( 'cctv_camera_failure', ['camera_hardware_failure', 'power_shortage'], 'or'),                                        
                                }

                self.base_gyro_failure_tree = {
                        'tree1': ('gyro_failure', ['hardware_failure', 'software_failure', 'power_shortage'], 'or'),
                        'tree6': ('hardware_failure', [], 'transfer'),
                        'tree7': ('software_failure', [], 'transfer'), 
                        }
                self.base_gps_failure_tree = {            
                                        'tree1': ( 'gps_failure', ['gps_hardware_failure', 'signal_jamming_general', 'gps_detection_failure', 'human_error'], 'or'),         
                                        'tree2': ('signal_jamming_general', ['signal_jamming', 'spoofing'], 'or'),
                                        'tree3': ('gps_hardware_failure', ['hardware_failure', 'rf_antenna_failure'], 'or'),
                                        'tree6': ('hardware_failure', [], 'transfer'),                              
                                        'tree5': ('human_error', [], 'transfer')
                                }

               
                self.base_gps_hardware_failure_tree = {            
                                        'tree1': ( 'base_gps_hardware_failure_tree', ['hardware_failure', 'rf_antenna_failure'], 'or'),
                                        'tree6': ('hardware_failure', [], 'transfer'),           
                                
                                }
                
                self.base_radar_failure_tree = {            
                                        'tree1': ( 'base_radar_failure', ['radar_hardware_failure', 'radar_detection_failure', ], 'or'),         
                                        'tree2': ('radar_hardware_failure', ['receiver_failure', 'rf_antenna_failure', 'power_shortage'], 'or'),
                                        
                                }
                self.base_radio_failure_tree = {            
                                'tree1': ( 'external_communication_failure', ['radio_hardware_failure', 'pc_failure', 'human_error'], 'or'),         
                                'tree2': ('radio_hardware_failure', ['rf_antenna_failure', 'receiver_failure'], 'or'),
                                'tree6': ('human_error', [], 'transfer'),  
                                  
                                
                        }
        
        def get_all_tress(self, ):   # TODO, use __dict__ instead of this abomination
                self.all_trees = [
                        self.base_radar_failure_tree,
                        self.base_hardware_failure_tree,
                        self.base_bridge_network_failure_tree, 
                        self.base_cctv_camera_failure_tree,
                        self.base_gps_failure_tree,
                        self.base_human_failure_tree,
                        self.base_radio_failure_tree,
                        self.base_software_failure_tree,
                        self.base_ais_failure_tree,
                        self.base_gps_hardware_failure_tree,
                        self.base_gyro_failure_tree,
                        ]
                return self.all_trees


class bzero_trees():
        def __init__(self,):
                '''Autolookout Sensor Failure'''
                self.autolookout_obj_sensor_tree = {     'tree1': ('autolookout_sensor_failure', ['1_failure', '2_failure', '4_failure'], 'or'),
                                    'tree2': ('1_failure', ['base_radar_failure', 'ais_failure'], 'and'),
                                    'tree3': ('2_failure', ['base_radar_failure', 'cctv_camera_failure'], 'and'),                                    
                                    'tree5': ('4_failure', ['ais_failure', 'cctv_camera_failure'], 'and'),                                   
                                    'tree8': ('ais_failure', [], 'transfer'),                               
                                    'tree11': ('cctv_camera_failure', [], 'transfer'),
                                    'tree12': ('base_radar_failure', [], 'transfer'),
                                    }
                '''Autolookout Fusion Failure'''
                self.autolookout_fusion_failure_tree = {  'tree1': ('autolookout_fusion_failure', ['autolookout_sensor_failure', 'gps_gyro_combo'], 'or'),
                                 'tree5': ('gps_gyro_combo', ['gps_failure', 'gyro_failure'], 'and'),
                                        'tree2': ('autolookout_sensor_failure', [], 'transfer'),
                                        'tree3': ('gps_failure', [], 'transfer'),
                                        'tree4': ('gyro_failure', [], 'transfer')  
                                    }
                '''Autolookout Object Detection Failure'''
                self.autolookout_object_detection_failure_tree = {  'tree1': ('autolookout_object_detection_failure', ['autolookout_sensor_failure', 'autolookout_software_based_detection_failure'], 'or'),
                                    'tree2': ('autolookout_sensor_failure', [], 'transfer'),
                                    # 'tree3': ('autolookout_software_based_detection_failure', [], 'transfer'),
                                    }
                
                '''Autolookout Object Assosication Failure'''
                self.autolookout_object_association_failure_tree = {  'tree1': ('autolookout_object_association_failure', ['autolookout_sensor_failure', 'autolookout_software_based_detection_failure'], 'or'),
                                    'tree2': ('autolookout_sensor_failure', [], 'transfer'),
                                #     'tree3': ('autolookout_software_based_fusion_algorithm_failure', [], 'transfer'),
                                    }

                '''Autolookout Fusion Failure'''
                self.autolookout_general_failure_tree = {  'tree1': ('autolookout_general_failure', ['autolookout_object_detection_failure', 'autolookout_object_association_failure'], 'or'),
                                        'tree2': ('autolookout_object_association_failure', [], 'transfer'),
                                          'tree4': ('autolookout_object_detection_failure', [], 'transfer')
                                    }
                
                '''Autolookout Object Tracker Failure'''
                self.autolookout_object_tracker_failure_tree = {  'tree1': ('autolookout_object_tracker_failure', ['software_failure', 'pc_failure'], 'or'),   
                                    
                                    'tree3': ('software_failure', [], 'transfer')                                      
                    
                                      }


                # ***AutoOOW Fault Trees***

                self.autooow_situational_awareness_failure_tree =  {  
            	                        'tree1': ('autooow_situational_awareness_failure', ['autolookout_object_tracker_failure', 'autolookout_general_failure', 'human_error'], 'or'),
                                          'tree3': ('autolookout_object_tracker_failure', [], 'transfer'),
                                          'tree4': ('autolookout_general_failure', [], 'transfer'),
                                          'tree5': ('human_error', [], 'transfer'),                                     
                                    }

                self.autooow_collision_avoidance_failure_tree = {  
                                          'tree1': ('autooow_collision_avoidance_failure', ['autooow_collision_avoidance_trajectory_prediction_failure', 'hardware_failure'], 'or'),
                                          'tree2': ('autooow_collision_avoidance_trajectory_prediction_failure', [ 'autooow_situational_awareness_failure', 'autooow_collision_avoidance_algorithm_failure', 'autolookout_object_tracker_failure', 'autooow_avoidance_trajectory_physically_not_possible'], 'or'),
                                          'tree3': ('autooow_situational_awareness_failure', [], 'transfer'),
                                          #'tree4': ('autooow_avoidance_trajectory_physically_not_possible', [], 'transfer'),
                                          #'tree5': ('autooow_collision_avoidance_algorithm_failure', [], 'transfer'),
                                          'tree6': ('hardware_failure', [], 'transfer'),
                                          'tree7': ('autolookout_object_tracker_failure', [], 'transfer')                                         
                                    }
                

                                                

                self.autooow_monitoring_failure_tree = { 'tree1': ('autooow_monitoring_failure', ['software_failure', 'hardware_failure', 'hacking'], 'or'),    
                                    'tree2': ('hardware_failure', [], 'transfer'),
                                    'tree3': ('software_failure', [], 'transfer'),                                                                       
                    
                                      }
                                                

                self.autooow_takeover_failure_tree = {  'tree1': ('autooow_takeover_failure', ['software_failure', 'hardware_failure'], 'or'),
                                            'tree2': ('hardware_failure', [], 'transfer'),
                                            'tree3': ('software_failure', [], 'transfer')                                         
                    
                                      }
                                                

               
                self.autooow_general_failure_tree = {  'tree1': ('autooow_general_failure', ['autooow_takeover_failure', 'autooow_monitoring_failure', 'autolookout_object_tracker_failure', 'autolookout_general_failure', 'autooow_collision_avoidance_failure', 'hacking'], 'or'),
                                        
                                         'tree3': ('autooow_takeover_failure', [], 'transfer'),
                                          'tree4': ('autooow_monitoring_failure', [], 'transfer'),
                                          'tree5': ('autolookout_object_tracker_failure', [], 'transfer'),
                                          'tree6': ('autolookout_general_failure', [], 'transfer'),
                                          'tree7': ('autooow_collision_avoidance_failure', [], 'transfer'),                                          
                                          
                                    }
                # ***BZERO Controller Fault Trees***

                self.bzero_controller_weather_sensor_failure_tree = {  'tree1': ('bzero_controller_weather_sensor_failure', ['hardware_failure', 'software_failure'], 'or'),        
                                                    'tree2': ('hardware_failure', [], 'transfer'),
                                    'tree3': ('software_failure', [], 'transfer')                                
                                    }
                self.bzero_controller_motion_sensor_failure_tree = {  'tree1': ('bzero_controller_motion_sensor_failure', ['hardware_failure', 'software_failure'], 'or'),
                                                    'tree2': ('hardware_failure', [], 'transfer'),
                                    'tree3': ('software_failure', [], 'transfer')  
                                    }                    

                self.bzero_controller_sensor_failure_tree = {  'tree1': ('bzero_controller_sensor_failure', ['bzero_controller_motion_sensor_failure', 'bzero_controller_weather_sensor_failure'], 'or'),        
                                            'tree2': ('bzero_controller_motion_sensor_failure', [], 'transfer'),
                                            'tree3': ('bzero_controller_weather_sensor_failure', [], 'transfer')                                
                                    }

                self.bzero_controller_general_failure_tree = {  'tree1': ('bzero_controller_general_failure', ['bridge_network_failure', 'machinery_failure', 'autooow_collision_avoidance_failure', 'bzero_controller_sensor_failure'], 'or'),
                                             'tree2': ('bridge_network_failure', [], 'transfer'),
                                             #'tree3': ('machinery_failure', [], 'transfer'),                                         
                                             'tree4': ('autooow_collision_avoidance_failure', [], 'transfer'),
                                             'tree5' : ('bzero_controller_sensor_failure', [], 'transfer')
                                          
                                    }

                
# checked and updated                  

                

                # ***BZERO HMI Fault Trees***

                self.bzero_hmi_alarm_failure_tree = {        'tree1': ( 'bzero_hmi_alarm_failure', ['hmi_monitor_failure', 'bridge_network_failure', 'bzero_transport_network_failure', 'smart_devices_failure'], 'or'),         
                                        #'tree4': ('hmi_monitor_failure', [], 'transfer'),                                      
                                        'tree5': ('bridge_network_failure', [], 'transfer'),
                                        #'tree6': ('bzero_transport_network_failure', [], 'transfer'),
                                        # 'tree7': ('smart_devices_failure', [], 'transfer')  
                                                }

                self.bzero_hmi_non_emergent_takeover_failure_tree = { 'tree1': ('bzero_hmi_non_emergent_takeover_failure', ['autooow_takeover_failure', 'human_error'], 'or'),
                                                'tree2': ('autooow_takeover_failure', [], 'transfer'),
                                                'tree3': ('human_error', [], 'transfer'),           
                                                }
                self.bzero_hmi_emergency_takeover_failure_tree = { 'tree1': ('bzero_hmi_emergency_takeover_failure', ['bzero_hmi_non_emergent_takeover_failure', 'bzero_hmi_alarm_failure'], 'or'),         
                                                'tree2': ('bzero_hmi_non_emergent_takeover_failure', [], 'transfer'),
                                                'tree3': ('bzero_hmi_alarm_failure', [], 'transfer'),}

                
                self.bzero_hmi_general_takeover_failure_tree = { 'tree1': ('bzero_hmi_general_takeover_failure', ['bzero_hmi_non_emergent_takeover_failure', 'bzero_hmi_emergency_takeover_failure'], 'or'),         
                                                'tree2': ('bzero_hmi_non_emergent_takeover_failure', [], 'transfer'),
                                                'tree3': ('bzero_hmi_emergency_takeover_failure', [], 'transfer'),}

        def get_all_tress(self, ):   
                self.all_trees = [self.bzero_hmi_alarm_failure_tree, 
                        self.bzero_controller_general_failure_tree, 
                        self.bzero_controller_motion_sensor_failure_tree, 
                        self.bzero_controller_weather_sensor_failure_tree, 
                        self.bzero_hmi_emergency_takeover_failure_tree, 
                        self.bzero_hmi_non_emergent_takeover_failure_tree,
                        self.autolookout_fusion_failure_tree,
                        self.autolookout_general_failure_tree,
                        self.autolookout_obj_sensor_tree,
                        self.autolookout_object_detection_failure_tree,
                        self.autooow_collision_avoidance_failure_tree,                       
                        self.autooow_general_failure_tree,
                        self.autooow_takeover_failure_tree,
                        self.autooow_monitoring_failure_tree,
                        self.autolookout_object_tracker_failure_tree,
                        self.autooow_situational_awareness_failure_tree, 
                        self.autolookout_object_association_failure_tree,
                        self.bzero_hmi_general_takeover_failure_tree,
                        self.bzero_controller_sensor_failure_tree,
                        ]
                return self.all_trees



                                
                                    