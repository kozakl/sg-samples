import shotgun_api3

sg = shotgun_api3.Shotgun('https://.shotgunstudio.com',
                          login='',
                          password='')

data = {
    'code': 'Test.mp4',
    'project': {
        'type': 'Project',
        'id': 127
    },
    'user': {'type': 'HumanUser', 'id': 87},
    'updated_by': {'type': 'HumanUser', 'id': 87},
    'sg_path_to_movie': '../Test.mp4'
}

version = sg.create('Version', data)
sg.upload('Version', version['id'], '../mats/test.mp4', 'sg_uploaded_movie')

#{'type': 'Project', 'name': '0000_sg_development', 'id': 127}
#{'type': 'Task', 'name': 'Modeldo', 'id': 7771}
#{'type': 'Asset', 'name': 'Teapot', 'id': 1605}
#W:\0000_sg_development\assets\art\Teapot\Mdl\aMdl\prev\Teapot_green_aMdl_v005.mp4
