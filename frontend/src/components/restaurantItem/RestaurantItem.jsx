import React from 'react'
import './RestaurantItem.css'
import StartRating from '../starRating/StartRating'
import CallIcon from '@mui/icons-material/Call';

const RestaurantItem = ({ restaurant }) => {
    return (
        <div className='restaurant-item-container'>
            <div className='restaurant-item-img-container'>
                <img align='middle' src={restaurant.image_url} className='restaurant-item-img' alt="not found" />
            </div>
            <div className='restaurant-item-info'>
                <div className='restaurant-item-name'>{restaurant.name}</div>
                <div className='restaurant-item-rating'>
                    <StartRating
                        count={restaurant.rating}
                        size={24}
                    />
                </div>
                <div className='restaurant-item-location'>{restaurant.location.address1}</div>
                <div className='restaurant-item-category'>{
                    restaurant.categories.map(category => {
                        return <div className='restaurant-item-category-chip' key={category.alias}> {category.title}</div>
                    })
                }</div>
                <div className='restaurant-item-status'>
                    {
                        restaurant.is_closed ?
                            <div style={{ color: 'red' }}>Closed</div> :
                            <div style={{ color: 'green' }}>Opening</div>
                    }
                </div>
                <div className='restaurant-item-telephone'>
                    <CallIcon fontSize='small' className='telephone-icon' />
                    <div>
                        {restaurant.phone ? restaurant.phone : 'No Available'}
                    </div>
                </div>
            </div>
        </div>

    )
}

export default RestaurantItem