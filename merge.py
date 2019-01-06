# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import arcpy
import os

source_folder = arcpy.GetParameterAsText(0)
target_folder = arcpy.GetParameterAsText(1)
file_names = arcpy.GetParameterAsText(2)

for x in os.listdir(source_folder):
    file_path = source_folder+'\\'+x
    if os.path.isfile(file_path):
        mdb_paths= os.path.split(file_path)
        mdb_names = mdb_paths[1].split('.')
        if mdb_names[-1]=='mdb':
            for file_name in [file_names]:
                feature_class = os.path.join(file_path,file_name)
                print feature_class

                if arcpy.Exists(feature_class):
                    for name in list(mdb_names):
                        if name != 'mdb':
                            arcpy.CopyFeatures_management(feature_class,target_folder+'\\'+'%s_%s.shp'%(os.path.splitext(name)[0],file_name))


