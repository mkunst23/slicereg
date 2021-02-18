import pytest
from numpy.ma import array, arange

from slicereg.models.section import Section, SliceImage, Plane


cases = [
    ((0, 0), (0., 0., 0.)),
    ((1, 1), (1., -1., 0.)),
]
@pytest.mark.parametrize("imcoord, atlascoord", cases)
def test_can_get_3d_position_from_2d_pixel_coordinate_in_section(imcoord, atlascoord):
    section = Section(
        image=SliceImage(
            channels=arange(18).reshape(2, 3, 3),
            pixel_resolution_um=1
        ),
        plane=Plane(x=0, y=0, theta=0),
    )
    i, j = imcoord
    x, y, z = atlascoord
    assert section.pos_from_coord(i=i, j=j) == (x, y, z)


@pytest.mark.parametrize("imcoords", [(-1, -1), (4, 0)])
def test_nonexistent_image_coords_raise_error(imcoords):
    section = Section(
        image=SliceImage(
            channels=arange(18).reshape(2, 3, 3),
            pixel_resolution_um=1
        ),
        plane=Plane(x=0, y=0, theta=0),
    )
    with pytest.raises(ValueError):
        i, j = imcoords
        section.pos_from_coord(i=i, j=j)