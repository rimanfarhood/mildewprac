import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_visualization_body():
    st.write('## Leaf Visualizer')
    st.info(
        f'The client is interested in having a study that visually'
        f'differentiates a a healthy cherry leaf from one that contains powdery mildew'
    )
    version = 'v1'
    if st.checkbox('Difference between average and variability image'):
        
        avg_healthy = plt.imread(f'outputs/{version}/avg_var_healthy.png')
        avg_mildew = plt.imread(f'outputs/{version}/avg_var_powdery_mildew.png')

        st.warning(f'f')

        st.image(avg_healthy, caption='Healthy leaf - Average and Variability')
        st.image(avg_mildew, caption='Mildew contained leaf - Average and Variability')
        st.write('---')
    
    if st.checkbox('Differences between average healthy cherry leaves and average Mildew contained leaves'):
        diff = plt.imread(f'outputs/{version}/avg_diff.png')

        st.warning(f'idk')
        st.image(diff, caption='Difference between average images')
    
    if st.checkbox('Image Montage'):
        st.write("* To refresh the montage, click on the 'Create Montage' button")
        data_dir = 'inputs/mildew_dataset/cherry-leaves'
        labels = os.listdir(data_dir+ '/validation')
        label_display = st.selectbox(label='Select Label', options=labels, index=0)
        if st.button('Create Montage'):
            image_montage(dir_path=data_dir + '/validation', 
                          label_display=label_display,
                          nrows=8, ncols=3, figsize=(10,25))
        st.write('---')

def image_montage(dir_path, label_display, nrows, ncols, figgsize=(15,10)):
    sns.set_Style(white)
    labels = os.listdir(dir_path)

    if label_display in labels:

        images_list = os.listdir(dir_path+'/'+ label_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return
        
        list_rows = range(0,nrows)
        list_cols = range(0,ncols)
        plot_idx = list(itertools.product(list_rows,list_cols))

        fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
        for x in range(0,nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()
        
        st.pyplot(fig=fig)
    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")

