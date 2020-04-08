
import React, { useState } from 'react'

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from 'react-slick';

const photos = [
    // {
    //     name: "image-1",
    //     url: "../../public/img/pic1.png",
    // },
    {
        name: "image-1",
        url: "https://images.unsplash.com/photo-1586115176276-3f7fe651ccf2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
    },
    {
        name: "image-1",
        url: "https://images.unsplash.com/photo-1536536982624-06c1776e0ca8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80",
    },
    {
        name: "image-1",
        url: "https://images.unsplash.com/photo-1545559054-8f4f9e855781?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80",
    },
    {
        name: "image-1",
        url: "https://images.unsplash.com/photo-1558258695-39d4595e049c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700&q=80",
    },
]

export default class TutorialPage extends React.Component {
    constructor() {
        super()

    }
    render() {
        const settings = {
            dots: true,
            fade: true,
            infinite: true,
            
            slidesToShow: 1,
            arrows: true,
            autoplay: true,
            speed: 500,
            autoplaySpeed: 2000,
            cssEase: "linear",
            slideToScroll: 1,
            className: "slides",
        }
        return (
            <div className="tutorial-container">
                <div className="tutorial-page-title-div">
                    <div className="tutorial-page-title-text">
                        <span className="title-text">
                            Tutorial Page
                        </span>
                    </div>
                </div>
                <div className="slider-container">
                    <Slider {...settings}
                    >
                        {photos.map((photo) => {
                            return (
                                <div className="image">
                                    <img src={photo.url} height="640" width="1280" />
                                </div>
                            )
                        })}

                    </Slider>
                </div>
                <div className="continue-button-div">
                    <div class="example_f_tutorial" align="center" >
                        <span>continue</span>
                    </div>
                </div>
            </div>
        )
    }
}