# ALL VALUE USE INT

## live_notes
- id : increase +1 each adding note
- call_time : format time in 30 FPS is 33.33333 MS
- note_type :
  - 1 - one button
  - 2 - hold
  - 3 - release
  - 4 - AC start*
  - 5 - AC end*
  * Types 4 and 5 are invisible in-game. They do not count towards combo or voltage. These notes only serve to mark the boundaries of ACs, and are placed up to 2 msec before or after the actual start/finish note of the AC.
- note_position :
  - 1 - left
  - 2 - right
- gimmick_id : follow up note_gimmicks id
- note_actions :
  - 1 - tap
  - 4 - swipe up
  - 5 - swipe down
  - 6 - swipe left
  - 7 - swipe right
- wave_id : follow up live_wave_settings id
- note_random_drop_color : 99 (default value)
- auto_judge_type : 20 (default value)
## live_wave_settings
- id : increase +1 each adding wave
- wave_damage : how many stamina damage value at fail
- mission_type : 
  - 1 - Gain Voltage! (x)
  - 2 - Get Nice or above (x) times!
  - 3 - Get Great or above (x) times!
  - 4 - Get (x) Wonderfuls! 
  - 5 - Get Voltage in one go!
  - 6 - Get (x) with an SP Skill!
  - 7 - Switch strategies and Appeal with (x) members!
  - 8 - Get a critical: x(x)
  - 9 - Activate a skill: x(x)
  - 16 - Maintain at least %(x) of your total Stamina.
- arg_1 : how many value of target AC
- arg_2 : 0 (default value)
- reward_voltage : Value Voltage at end AC
