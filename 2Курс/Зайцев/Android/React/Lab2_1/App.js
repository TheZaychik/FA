import * as React from 'react';
import {Text, View, Image, StyleSheet} from 'react-native';
import Constants from 'expo-constants';

// You can import from local files
import AssetExample from './components/AssetExample';

// or any pure javascript modules available in npm
import {Card} from 'react-native-paper';

export default function App() {
    return (
        <View style={styles.container}>
            <Text style={styles.paragraph}>
                Журнал Lorem
            </Text>
            <Card>
                <Text style={styles.blue}>
                    Ipsum
                </Text>
                <Image
                    source={{uri: 'https://a-static.besthdwallpaper.com/udivitel-nyy-vid-gor-oboi-3200x2400-11230_29.jpg',}}
                    style={{margin: 10, width: 200, height: 200}}
                />
                <Text style={styles.Bigtxt}>
                    Lorem ipsum dolor sit amet
                </Text>
                <Text style={styles.txt}>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi auctor erat eget tellus sollicitudin,
                    sed ullamcorper neque egestas. Sed placerat mi nec eros placerat, vel porttitor purus mattis. Donec
                    tellus ante, blandit eget posuere non, rhoncus pellentesque purus. Integer vitae erat justo. Vivamus
                    lacinia risus vel tristique luctus. Nam a ipsum elementum, suscipit leo in, semper velit. Nunc
                    gravida quam nec justo malesuada, sed consequat massa iaculis. Sed rhoncus, mauris sed pellentesque
                    ultricies, eros nisi tincidunt felis, ac rhoncus elit augue vestibulum ligula. Cras neque quam,
                    ornare in risus ac, auctor ornare leo. Pellentesque sed tellus pellentesque ligula auctor
                    scelerisque ut at justo. Fusce id ipsum non magna lacinia posuere at eu orci. Integer ut dolor nisl.
                    Nunc ac faucibus dolor, hendrerit vehicula purus. Aliquam commodo ullamcorper risus nec tincidunt.
                    Mauris aliquam quam eget est rhoncus, at laoreet nisi ultrices. Duis pretium venenatis odio,
                    vulputate tincidunt eros gravida et.
                </Text>
            </Card>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        paddingTop: Constants.statusBarHeight,
        backgroundColor: '#ecf0f1',
        padding: 8,
    },
    paragraph: {
        margin: 24,
        fontSize: 18,
        fontWeight: 'bold',
        textAlign: 'center',
    },
    blue: {
        margin: 10,
        color: 'blue',
    },
    txt: {
        margin: 10,
    },
    Bigtxt: {
        fontWeight: 'bold',
        margin: 10,
    }
});

