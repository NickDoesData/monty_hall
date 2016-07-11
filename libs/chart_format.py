def format_line_chart(df, index=True, width=9,height=7,title='', subtitle='',note='', \
                              title_font_size=16,axis_font_size=13,legend_loc='', title_shift=0, note_shift=0, gridlines=''):
    
    import matplotlib.pyplot as plt  
    import numpy as np
    
    title_color = (21/255.,75/255.,119/255.)
     # These are the "Tableau 20" colors as RGB.    
    tableau20 = [ (31, 119, 180),  (255, 127, 14),     
                 (44, 160, 44), (214, 39, 40),     
                 (148, 103, 189),(140, 86, 75),  
                 (227, 119, 194), (127, 127, 127),    
                 (188, 189, 34),  (23, 190, 207),
                 (174, 199, 232),(255, 187, 120),
                 (152, 223, 138),(255, 152, 150),
                 (197, 176, 213), (196, 156, 148),
                 (247, 182, 210),(199, 199, 199),
                (219, 219, 141), (158, 218, 229),]    

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
    for i  in range(len(tableau20)):    
        r, g, b = tableau20[i]    
        tableau20[i] = (r / 255., g / 255., b / 255.)    

  
    fig = plt.figure(figsize=(width, height))    

    # Remove the plot frame lines. They are unnecessary chartjunk.    
    #subplot 111 indicates no subplots
    ax = plt.subplot(111)    
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)    

    # Ensure that the axis ticks only show up on the bottom and left of the plot.    
    # Ticks on the right and top of the plot are generally unnecessary chartjunk.    
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()    

    # Provide tick lines across the plot to help your viewers trace along    
    # the axis ticks. Make sure that the lines are light and small so they    
    # don't obscure the primary data lines.    
    
    xmin = df.index.min()
    xmax = df.index.max()
    for y in range(0, 101, 20):    
        plt.plot(range(xmin,xmax), [y] * len(range(xmin, xmax)), "--", lw=0.5, color="black", alpha=0.3)   
    
    
    # Make sure your axis ticks are large enough to be easily read.    
    # You don't want your viewers squinting to read your plot.    
    plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)    
    plt.xticks(fontsize=14)    
    plt.yticks(fontsize=14)
    
    plt.xlabel("number of simulations", fontsize=14)

    # Remove the tick marks; they are unnecessary with the tick lines we just plotted.    
    plt.tick_params(axis="both", which="both", bottom="off", top="off",    
                    labelbottom="on", left="off", right="off", labelleft="on")    

    cols = df.columns   

    for rank, column in enumerate(cols):    
        # Plot each line separately with its own color, using the Tableau 20    
        # color set in order.    
        plt.plot(df.index,    
                df[column].values,    
                lw=2.5, color=tableau20[rank])    

        # Add a text label to the right end of every line. Most of the code below    
        # is adding specific offsets y position because some labels overlapped.    
        y_pos = df[column].values[-1]
        x_pos = df.index.max() + 1  
  
        
        # Again, make sure that all labels are large enough to be easily read    
        # by the viewer.    
        plt.text(max(df.index) + 1, y_pos, column, fontsize=14, color=tableau20[rank])    



    # Note that if the title is descriptive enough, it is unnecessary to include        
    plt.text(np.median(df.index), max(ax.get_ylim()) + 5, title, fontsize=16, ha="center", style='normal')    

    
    if note <> '': 
        plt.text(min(df.index), min(ax.get_ylim())-5, note, fontsize=10)    
 

    return fig