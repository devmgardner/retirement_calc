#############################################################################
# Generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#  Apr 24, 2023 04:41:14 PM EDT  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m45" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1024x708+370+156
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1920 1061
    wm minsize $top 640 480
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Retirement Calculator"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "calc_window" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu "$top.m45" \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font "TkMenuFont" -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
### SPOT dump_widget_opt A
    
set site_3_0 $top.m45
    $top.m45 add cascade \
        -menu "$top.m45.men46" -label "Reports" 
    menu "$site_3_0.men46" \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font "TkMenuFont" -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
### SPOT dump_widget_opt A
    $site_3_0.men46 add command \
        -command "#" -label "Save Report" 
    frame "$top.fra47" \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.fra47" "data_frame" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.fra47
    text "$site_3_0.tex61" \
        -background white -font "TkTextFont" -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 64 -wrap word 
    $site_3_0.tex61 configure -font "TkTextFont"
    $site_3_0.tex61 insert end text
    vTcl:DefineAlias "$site_3_0.tex61" "year1_401k_text" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $site_3_0.tex61
    label "$site_3_0.lab62" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "401k" 
    vTcl:DefineAlias "$site_3_0.lab62" "year1_401k_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $site_3_0.lab62
    text "$site_3_0.tex63" \
        -background white -font "TkTextFont" -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 64 -wrap word 
    $site_3_0.tex63 configure -font "TkTextFont"
    $site_3_0.tex63 insert end text
    vTcl:DefineAlias "$site_3_0.tex63" "year1_match_text" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $site_3_0.tex63
    label "$site_3_0.lab64" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Match" 
    vTcl:DefineAlias "$site_3_0.lab64" "year1_match_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $site_3_0.lab64
    text "$site_3_0.tex65" \
        -background white -font "TkTextFont" -foreground black -height 4 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 10 -wrap word 
    $site_3_0.tex65 configure -font "TkTextFont"
    $site_3_0.tex65 insert end text
    vTcl:DefineAlias "$site_3_0.tex65" "year1_savings_text" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab67" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Savings" 
    vTcl:DefineAlias "$site_3_0.lab67" "year1_savings_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $site_3_0.lab67
    text "$site_3_0.tex68" \
        -background white -font "TkTextFont" -foreground black -height 4 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 10 -wrap word 
    $site_3_0.tex68 configure -font "TkTextFont"
    $site_3_0.tex68 insert end text
    vTcl:DefineAlias "$site_3_0.tex68" "year1_total_text" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $site_3_0.tex68
    label "$site_3_0.lab69" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Year Saved" 
    vTcl:DefineAlias "$site_3_0.lab69" "year1_total_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $site_3_0.lab69
    text "$site_3_0.tex47" \
        -background white -font "TkTextFont" -foreground black -height 4 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 10 -wrap word 
    $site_3_0.tex47 configure -font "TkTextFont"
    $site_3_0.tex47 insert end text
    vTcl:DefineAlias "$site_3_0.tex47" "year1_full_total_text" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab48" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Total Saved" 
    vTcl:DefineAlias "$site_3_0.lab48" "year1_full_total_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    place $site_3_0.tex61 \
        -in $site_3_0 -x 0 -relx 0.013 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.104 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab62 \
        -in $site_3_0 -x 0 -relx 0.13 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.044 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tex63 \
        -in $site_3_0 -x 0 -relx 0.182 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.083 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab64 \
        -in $site_3_0 -x 0 -relx 0.28 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.065 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tex65 \
        -in $site_3_0 -x 0 -relx 0.345 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.104 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab67 \
        -in $site_3_0 -x 0 -relx 0.462 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.072 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tex68 \
        -in $site_3_0 -x 0 -relx 0.534 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.104 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab69 \
        -in $site_3_0 -x 0 -relx 0.651 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.086 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tex47 \
        -in $site_3_0 -x 0 -relx 0.749 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.104 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.866 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.086 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    vTcl:copy_lock $top.fra47
    entry "$top.ent49" \
        -background white -disabledforeground #a3a3a3 -font "TkFixedFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 10 
    vTcl:DefineAlias "$top.ent49" "years_entry" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.ent49
    label "$top.lab50" \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Years" 
    vTcl:DefineAlias "$top.lab50" "years_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.lab50
    button "$top.but51" \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Update" 
    vTcl:DefineAlias "$top.but51" "years_button" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.but51
    entry "$top.ent53" \
        -background white -disabledforeground #a3a3a3 -font "TkFixedFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$top.ent53" "salary_entry" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.ent53
    label "$top.lab54" \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Salary" 
    vTcl:DefineAlias "$top.lab54" "salary_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.lab54
    button "$top.but55" \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Update" 
    vTcl:DefineAlias "$top.but55" "salary_button" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.but55
    entry "$top.ent56" \
        -background white -disabledforeground #a3a3a3 -font "TkFixedFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$top.ent56" "raise_entry" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.ent56
    label "$top.lab48" \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Raise" 
    vTcl:DefineAlias "$top.lab48" "raise_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.lab48
    button "$top.but49" \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Update" 
    vTcl:DefineAlias "$top.but49" "raise_button" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.but49
    entry "$top.ent50" \
        -background white -disabledforeground #a3a3a3 -font "TkFixedFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$top.ent50" "_401k_entry" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.ent50
    label "$top.lab51" \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "401k" 
    vTcl:DefineAlias "$top.lab51" "_401k_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.lab51
    button "$top.but52" \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Update" 
    vTcl:DefineAlias "$top.but52" "_401k_button" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.but52
    entry "$top.ent54" \
        -background white -disabledforeground #a3a3a3 -font "TkFixedFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$top.ent54" "match_entry" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.ent54
    label "$top.lab55" \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Match" 
    vTcl:DefineAlias "$top.lab55" "match_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.lab55
    button "$top.but56" \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Update" 
    vTcl:DefineAlias "$top.but56" "match_button" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.but56
    entry "$top.ent58" \
        -background white -disabledforeground #a3a3a3 -font "TkFixedFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$top.ent58" "savings_entry" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.ent58
    label "$top.lab59" \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Savings" 
    vTcl:DefineAlias "$top.lab59" "savings_label" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.lab59
    button "$top.but60" \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font "TkDefaultFont" -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Update" 
    vTcl:DefineAlias "$top.but60" "savings_buton" vTcl:WidgetProc "calc_window" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.but60
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra47 \
        -in $top -x 0 -relx 0.01 -y 0 -rely 0.009 -width 0 -relwidth 0.75 \
        -height 0 -relheight 0.975 -anchor nw -bordermode ignore 
    place $top.ent49 \
        -in $top -x 0 -relx 0.775 -y 0 -rely 0.009 -width 75 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 0 -relx 0.862 -y 0 -rely 0.009 -width 0 -relwidth 0.031 \
        -height 0 -relheight 0.027 -anchor nw -bordermode ignore 
    place $top.but51 \
        -in $top -x 0 -relx 0.91 -y 0 -rely 0.009 -width 65 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent53 \
        -in $top -x 0 -relx 0.775 -y 0 -rely 0.053 -width 75 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 0 -relx 0.862 -y 0 -rely 0.053 -width 0 -relwidth 0.034 \
        -height 0 -relheight 0.027 -anchor nw -bordermode ignore 
    place $top.but55 \
        -in $top -x 0 -relx 0.91 -y 0 -rely 0.053 -width 65 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent56 \
        -in $top -x 0 -relx 0.775 -y 0 -rely 0.098 -width 75 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.862 -y 0 -rely 0.098 -width 0 -relwidth 0.034 \
        -height 0 -relheight 0.026 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 0 -relx 0.91 -y 0 -rely 0.098 -width 65 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent50 \
        -in $top -x 0 -relx 0.775 -y 0 -rely 0.141 -width 75 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 0 -relx 0.862 -y 0 -rely 0.141 -width 0 -relwidth 0.034 \
        -height 0 -relheight 0.026 -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 0 -relx 0.91 -y 0 -rely 0.141 -width 65 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent54 \
        -in $top -x 0 -relx 0.775 -y 0 -rely 0.185 -width 75 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 0 -relx 0.862 -y 0 -rely 0.185 -width 0 -relwidth 0.034 \
        -height 0 -relheight 0.026 -anchor nw -bordermode ignore 
    place $top.but56 \
        -in $top -x 0 -relx 0.91 -y 0 -rely 0.185 -width 65 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent58 \
        -in $top -x 0 -relx 0.775 -y 0 -rely 0.229 -width 75 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab59 \
        -in $top -x 0 -relx 0.859 -y 0 -rely 0.229 -width 0 -relwidth 0.044 \
        -height 0 -relheight 0.026 -anchor nw -bordermode ignore 
    place $top.but60 \
        -in $top -x 0 -relx 0.91 -y 0 -rely 0.229 -width 65 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top44 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

