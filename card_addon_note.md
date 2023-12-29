# table need to be added (WIP never be planned or not)
## m_active_skill
  - id : main
  - skill_type :
    - 1 - Voltage
    - 2 - Parameter
    - 3 - SpecialBuff
    - 4 - Debuff
    - 5 - Stamina
    - 6 - DamageReduce
  - skill_rarity_type
    - 1 - SkillRankD *common
    - 2 - SkillRankC
    - 3 - SkillRankB
    - 4 - SkillRankA
    - 5 - SkillRankS
  - skill_master_id : follow up m_skill table
  - name :
  - description :
  - sp_gauge_point :
  - trigger_probability :
  - icon_asset_path : NULL
  - thumbnail_asset_path :
    
## m_card
- id : main
- member_m_id : chara_id
- school_idol_no : add +1
- card_rarity_type :
  - 10 - Rare | R
  - 20 - SRare | SR
  - 30 - URare | UR
- card_attribute :
  - 1 - Smile
  - 2 - Pure
  - 3 - Cool
  - 4 - Active
  - 5 - Natural
  - 6 - Elegant
  - 9 - No Attribute
- role :
  - 1 - Boost | VO
  - 2 - Charge | SP
  - 3 - Heal | GD
  - 4 - Support | SK
- member_card_thumbnail_asset_path : >i (default SR & UR)
- at_gacha : 1 - your card is gacha
- at_event : 1 - your card is event
- training_tree_m_id : 
- active_skill_voice_path : sheets_name
- sp_point :
  1 - R
  2 - SR
  3 - UR
  4 - UR (Limited)
- exchange_item_id :
  - 1 - R
  - 2 - SR
  - 3 - UR
- role_effect_master_id : follow up role row
- passive_skill_slot :
- max_passive_skill_slot :
