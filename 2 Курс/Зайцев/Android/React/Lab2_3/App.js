import * as React from 'react';
import {Text, View, StyleSheet, Button} from 'react-native';
import Constants from 'expo-constants';

// You can import from local files
import AssetExample from './components/AssetExample';

// or any pure javascript modules available in npm
import {Card} from 'react-native-paper';

export default function App() {
    return (
        <View style={styles.container}>
            <Text style={styles.paragraph}>
                Mauris ut risus erat.
            </Text>
            <Card>
                <Text style={styles.center}>
                    Fusce sagittis justo placerat enim temporFusce sagittis justo placerat enim tempor
                </Text>
                <Card style={{backgroundColor: '#808080'}}>
                    <Text style={{flex: 3}}>
                        Mauris ut risus erat. Fusce sagittis justo placerat enim tempor, quis hendrerit risus commodo.
                        Nullam vestibulum porta magna, in fringilla risus pellentesque id. In eu elementum turpis. Sed
                        vulputate leo ac fermentum blandit. Mauris vitae lacus sem. Nulla felis dui, vehicula iaculis
                        malesuada ac, rhoncus in nibh. Quisque libero ligula, interdum at eleifend non, dapibus aliquam
                        neque. Curabitur a neque sollicitudin, aliquam dolor sit amet, venenatis urna. Aliquam mollis,
                        justo non hendrerit imperdiet, tellus arcu scelerisque nunc, scelerisque mattis sapien libero id
                        tortor. Duis nec nibh at enim consectetur facilisis sit amet a sapien. Cras venenatis imperdiet
                        erat quis molestie. Vestibulum ullamcorper, mauris sit amet tincidunt scelerisque, risus dui
                        mollis libero, a mattis nulla libero eget nisi.
                    </Text>
                    <Button
                        title="Learn More"
                        color="#841584"
                        accessibilityLabel="Learn more about this purple button"
                    />
                </Card>
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
    center: {
        margin: 24,
        fontSize: 18,
        textAlign: 'center',
        flex: 1,
    },
});
